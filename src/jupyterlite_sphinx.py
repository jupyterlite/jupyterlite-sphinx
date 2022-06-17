import os
import shutil
import tempfile

from pathlib import Path

from urllib.parse import quote

import subprocess

from docutils.parsers.rst import directives
from docutils.nodes import SkipNode, Element
from docutils.parsers import rst

from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective
from sphinx.parsers import RSTParser


CONTENT_DIR = "_contents"
JUPYTERLITE_DIR = "lite"

IFRAME_STYLE = "border-width: 1px; border-style: solid;"


# Used for nodes that do not need to be rendered
def skip(self, node):
    raise SkipNode


# Used to render an element node as HTML
def visit_element_html(self, node):
    self.body.append(node.html())
    raise SkipNode


class RepliteIframe(Element):
    """Appended to the doctree by the RepliteDirective directive

    Renders an iframe that shows a replite console.
    """

    def __init__(
        self,
        rawsource="",
        *children,
        prefix=JUPYTERLITE_DIR,
        width="100%",
        height="100%",
        content=[],
        replite_options=None,
        **attributes,
    ):
        super().__init__(
            "",
            prefix=prefix,
            width=width,
            height=height,
            content=content,
            replite_options=replite_options,
        )

    def html(self):
        replite_options = self["replite_options"]

        # Remove empty lines
        code_lines = ["" if not line.strip() else line for line in self["content"]]
        code = "\n".join(code_lines)

        replite_options["code"] = code

        options = "&".join(
            [f"{key}={quote(value)}" for key, value in replite_options.items()]
        )

        return (
            f'<iframe src="{self["prefix"]}/repl/index.html?{options}"'
            f'width="{self["width"]}" height="{self["height"]}" style="{IFRAME_STYLE}"></iframe>'
        )


class RepliteDirective(SphinxDirective):
    """The ``.. replite::`` directive.

    Adds a replite console to the docs.
    """

    has_content = True
    required_arguments = 0
    option_spec = {
        "width": directives.unchanged,
        "height": directives.unchanged,
        "kernel": directives.unchanged,
        "toolbar": directives.unchanged,
        "theme": directives.unchanged,
    }

    def run(self):
        width = self.options.pop("width", "100%")
        height = self.options.pop("height", "100%")

        prefix = os.path.relpath(
            os.path.join(self.env.app.srcdir, JUPYTERLITE_DIR),
            os.path.dirname(self.get_source_info()[0]),
        )

        return [
            RepliteIframe(
                prefix=prefix,
                width=width,
                height=height,
                content=self.content,
                replite_options=self.options,
            )
        ]


class _LiteIframe(Element):
    def __init__(
        self,
        rawsource="",
        *children,
        prefix=JUPYTERLITE_DIR,
        width="100%",
        height="1000px",
        notebook=None,
        **attributes,
    ):
        super().__init__(
            "", prefix=prefix, notebook=notebook, width=width, height=height
        )

    def html(self):
        notebook = self["notebook"]

        src = (
            f'{self["prefix"]}/{self.lite_app}/{self.notebooks_path}?path={notebook}'
            if notebook is not None
            else f'{self["prefix"]}/{self.lite_app}'
        )

        return (
            f'<iframe src="{src}"'
            f'width="{self["width"]}" height="{self["height"]}" style="{IFRAME_STYLE}"></iframe>'
        )


class JupyterLiteIframe(_LiteIframe):
    """Appended to the doctree by the JupyterliteDirective directive

    Renders an iframe that shows a Notebook with JupyterLite.
    """

    lite_app = "lab"
    notebooks_path = ""


class RetroLiteIframe(_LiteIframe):
    """Appended to the doctree by the RetroliteDirective directive

    Renders an iframe that shows a Notebook with RetroLite.
    """

    lite_app = "retro"
    notebooks_path = "notebooks/"


class _LiteDirective(SphinxDirective):

    has_content = False
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        "width": directives.unchanged,
        "height": directives.unchanged,
    }

    def run(self):
        width = self.options.get("width", "100%")
        height = self.options.get("height", "1000px")

        source_location = os.path.dirname(self.get_source_info()[0])

        prefix = os.path.relpath(
            os.path.join(self.env.app.srcdir, JUPYTERLITE_DIR), source_location
        )

        if self.arguments:
            # As with other directives like literalinclude, an absolute path is
            # assumed to be relative to the document root, and a relative path
            # is assumed to be relative to the source file
            rel_filename, notebook = self.env.relfn2path(self.arguments[0])
            self.env.note_dependency(rel_filename)

            notebook_name = os.path.basename(notebook)

            notebooks_dir = Path(self.env.app.srcdir) / CONTENT_DIR / notebook_name

            # Copy the Notebook for RetroLite to find
            os.makedirs(os.path.dirname(notebooks_dir), exist_ok=True)
            shutil.copyfile(notebook, str(notebooks_dir))
        else:
            notebook_name = None

        return [
            self.iframe_cls(
                prefix=prefix, notebook=notebook_name, width=width, height=height
            )
        ]


class JupyterLiteDirective(_LiteDirective):
    """The ``.. jupyterlite::`` directive.

    Renders a Notebook with JupyterLite in the docs.
    """

    iframe_cls = JupyterLiteIframe


class RetroLiteDirective(_LiteDirective):
    """The ``.. retrolite::`` directive.

    Renders a Notebook with RetroLite in the docs.
    """

    iframe_cls = RetroLiteIframe


class RetroLiteParser(RSTParser):
    """Sphinx source parser for Jupyter notebooks.

    Shows the Notebook using retrolite."""

    supported = ("jupyterlite_notebook",)

    def parse(self, inputstring, document):
        title = os.path.splitext(os.path.basename(document.current_source))[0]
        # Make the "absolute" filename relative to the source root
        filename = "/" + os.path.relpath(document.current_source, self.env.app.srcdir)
        super().parse(
            f"{title}\n{'=' * len(title)}\n.. retrolite:: {filename}",
            document,
        )


def inited(app: Sphinx, config):
    # Create the content dir
    os.makedirs(os.path.join(app.srcdir, CONTENT_DIR), exist_ok=True)

    if (
        ".ipynb" not in config.source_suffix
        and ".ipynb" not in app.registry.source_suffix
    ):
        app.add_source_suffix(".ipynb", "jupyterlite_notebook")


def jupyterlite_build(app: Sphinx, error):
    if error is not None:
        # Do not build JupyterLite
        return

    if app.builder.format == "html":
        print("[jupyterlite-sphinx] Running JupyterLite build")

        config = []
        if app.env.config.jupyterlite_config:
            config = ["--config", app.env.config.jupyterlite_config]

        with tempfile.TemporaryDirectory() as tmp_dir:
            subprocess.run(
                [
                    "jupyter",
                    "lite",
                    "build",
                    "--debug",
                    *config,
                    "--lite-dir",
                    tmp_dir,
                    "--contents",
                    os.path.join(app.srcdir, CONTENT_DIR),
                    "--output-dir",
                    os.path.join(app.outdir, JUPYTERLITE_DIR),
                ],
                check=True,
            )

        print("[jupyterlite-sphinx] JupyterLite build done")

    # Cleanup
    try:
        shutil.rmtree(os.path.join(app.srcdir, CONTENT_DIR))
        os.remove(".jupyterlite.doit.db")
    except FileNotFoundError:
        pass


def setup(app):
    # Initialize RetroLite parser
    app.add_source_parser(RetroLiteParser)

    app.connect("config-inited", inited)
    # We need to build JupyterLite at the end, when all the content was created
    app.connect("build-finished", jupyterlite_build)

    # Config options
    app.add_config_value("jupyterlite_config", None, rebuild="html")

    # Initialize RetroLite and JupyterLite directives
    app.add_node(
        RetroLiteIframe,
        html=(visit_element_html, None),
        latex=(skip, None),
        textinfo=(skip, None),
        text=(skip, None),
        man=(skip, None),
    )
    app.add_directive("retrolite", RetroLiteDirective)
    app.add_node(
        JupyterLiteIframe,
        html=(visit_element_html, None),
        latex=(skip, None),
        textinfo=(skip, None),
        text=(skip, None),
        man=(skip, None),
    )
    app.add_directive("jupyterlite", JupyterLiteDirective)

    # Initialize Replite directive
    app.add_node(
        RepliteIframe,
        html=(visit_element_html, None),
        latex=(skip, None),
        textinfo=(skip, None),
        text=(skip, None),
        man=(skip, None),
    )
    app.add_directive("replite", RepliteDirective)
