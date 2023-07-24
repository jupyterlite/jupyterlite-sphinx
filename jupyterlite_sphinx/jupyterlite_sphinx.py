import os
from uuid import uuid4
import shutil
import tempfile
from warnings import warn
import glob

from pathlib import Path

from urllib.parse import quote

import subprocess

from docutils.parsers.rst import directives
from docutils.nodes import SkipNode, Element

from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective
from sphinx.util.fileutil import copy_asset
from sphinx.parsers import RSTParser

try:
    import voici
except ImportError:
    voici = None

HERE = Path(__file__).parent

CONTENT_DIR = "_contents"
JUPYTERLITE_DIR = "lite"


# Used for nodes that do not need to be rendered
def skip(self, node):
    raise SkipNode


# Used to render an element node as HTML
def visit_element_html(self, node):
    self.body.append(node.html())
    raise SkipNode


class _PromptedIframe(Element):
    def __init__(
        self,
        rawsource="",
        *children,
        iframe_src="",
        width="100%",
        height="100%",
        prompt=False,
        prompt_color=None,
        **attributes,
    ):
        super().__init__(
            "",
            iframe_src=iframe_src,
            width=width,
            height=height,
            prompt=prompt,
            prompt_color=prompt_color,
        )

    def html(self):
        iframe_src = self["iframe_src"]

        if self["prompt"]:
            prompt = (
                self["prompt"] if isinstance(self["prompt"], str) else "Try It Live!"
            )
            prompt_color = (
                self["prompt_color"] if self["prompt_color"] is not None else "#f7dc1e"
            )

            placeholder_id = uuid4()
            container_style = f'width: {self["width"]}; height: {self["height"]};'

            return (
                f"<div class=\"jupyterlite_sphinx_iframe_container\" style=\"{container_style}\" onclick=window.jupyterliteShowIframe('{placeholder_id}','{iframe_src}')>"
                f'  <div id={placeholder_id} class="jupyterlite_sphinx_try_it_button jupyterlite_sphinx_try_it_button_unclicked" style="background-color: {prompt_color};">'
                f"    {prompt}"
                "   </div>"
                "</div>"
            )

        return (
            f'<iframe src="{iframe_src}"'
            f'width="{self["width"]}" height="{self["height"]}" class="jupyterlite_sphinx_raw_iframe"></iframe>'
        )


class _LiteIframe(_PromptedIframe):
    def __init__(
        self,
        rawsource="",
        *children,
        prefix=JUPYTERLITE_DIR,
        content=[],
        notebook=None,
        lite_options={},
        **attributes,
    ):
        if content:
            code_lines = ["" if not line.strip() else line for line in content]
            code = "\n".join(code_lines)

            lite_options["code"] = code

        app_path = self.lite_app
        if notebook is not None:
            lite_options["path"] = notebook
            app_path = f"{self.lite_app}{self.notebooks_path}"

        options = "&".join(
            [f"{key}={quote(value)}" for key, value in lite_options.items()]
        )

        iframe_src = f'{prefix}/{app_path}{f"?{options}" if options else ""}'

        super().__init__(rawsource, *children, iframe_src=iframe_src, **attributes)


class RepliteIframe(_LiteIframe):
    """Appended to the doctree by the RepliteDirective directive

    Renders an iframe that shows a repl with JupyterLite.
    """

    lite_app = "repl/index.html"
    notebooks_path = ""


class JupyterLiteIframe(_LiteIframe):
    """Appended to the doctree by the JupyterliteDirective directive

    Renders an iframe that shows a Notebook with JupyterLite.
    """

    lite_app = "lab/"
    notebooks_path = ""


class RetroLiteIframe(_LiteIframe):
    """Appended to the doctree by the RetroliteDirective directive

    Renders an iframe that shows a Notebook with RetroLite.
    """

    lite_app = "retro/"
    notebooks_path = "notebooks/"


class VoiciIframe(_PromptedIframe):
    """Appended to the doctree by the VoiciDirective directive

    Renders an iframe that shows a Notebook with Voici.
    """

    def __init__(
        self,
        rawsource="",
        *children,
        prefix=JUPYTERLITE_DIR,
        notebook=None,
        lite_options={},
        **attributes,
    ):
        if notebook is not None:
            app_path = f"voici/render/{notebook.replace('.ipynb', '.html')}"
        else:
            app_path = "voici/tree"

        options = "&".join(
            [f"{key}={quote(value)}" for key, value in lite_options.items()]
        )

        iframe_src = f'{prefix}/{app_path}{f"?{options}" if options else ""}'

        super().__init__(rawsource, *children, iframe_src=iframe_src, **attributes)


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
        "prompt": directives.unchanged,
        "prompt_color": directives.unchanged,
    }

    def run(self):
        width = self.options.pop("width", "100%")
        height = self.options.pop("height", "100%")

        prompt = self.options.pop("prompt", False)
        prompt_color = self.options.pop("prompt_color", None)

        prefix = os.path.relpath(
            os.path.join(self.env.app.srcdir, JUPYTERLITE_DIR),
            os.path.dirname(self.get_source_info()[0]),
        )

        return [
            RepliteIframe(
                prefix=prefix,
                width=width,
                height=height,
                prompt=prompt,
                prompt_color=prompt_color,
                content=self.content,
                lite_options=self.options,
            )
        ]


class _LiteDirective(SphinxDirective):
    has_content = False
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        "width": directives.unchanged,
        "height": directives.unchanged,
        "theme": directives.unchanged,
        "prompt": directives.unchanged,
        "prompt_color": directives.unchanged,
    }

    def run(self):
        width = self.options.pop("width", "100%")
        height = self.options.pop("height", "1000px")

        prompt = self.options.pop("prompt", False)
        prompt_color = self.options.pop("prompt_color", None)

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
            try:
                shutil.copyfile(notebook, str(notebooks_dir))
            except shutil.SameFileError:
                pass
        else:
            notebook_name = None

        return [
            self.iframe_cls(
                prefix=prefix,
                notebook=notebook_name,
                width=width,
                height=height,
                prompt=prompt,
                prompt_color=prompt_color,
                lite_options=self.options,
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


class VoiciDirective(_LiteDirective):
    """The ``.. voici::`` directive.

    Renders a Notebook with Voici in the docs.
    """

    iframe_cls = VoiciIframe

    def run(self):
        if voici is None:
            raise RuntimeError(
                "Voici must be installed if you want to make use of the voici directive: pip install voici"
            )

        return super().run()


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
        config.jupyterlite_bind_ipynb_suffix
        and ".ipynb" not in config.source_suffix
        and ".ipynb" not in app.registry.source_suffix
    ):
        app.add_source_suffix(".ipynb", "jupyterlite_notebook")


def jupyterlite_build(app: Sphinx, error):
    if error is not None:
        # Do not build JupyterLite
        return

    if app.builder.format == "html":
        print("[jupyterlite-sphinx] Running JupyterLite build")
        jupyterlite_config = app.env.config.jupyterlite_config
        jupyterlite_contents = app.env.config.jupyterlite_contents
        jupyterlite_dir = app.env.config.jupyterlite_dir

        config = []
        if jupyterlite_config:
            config = ["--config", jupyterlite_config]

        if jupyterlite_contents is None:
            jupyterlite_contents = []
        elif isinstance(jupyterlite_contents, str):
            jupyterlite_contents = [jupyterlite_contents]

        # Expand globs in the contents strings
        jupyterlite_contents = [
            match
            for pattern in jupyterlite_contents
            for match in glob.glob(pattern, recursive=True)
        ]

        contents = []
        for content in jupyterlite_contents:
            contents.extend(["--contents", content])

        voici_option = [] if voici is None else ["--apps", "voici"]

        command = [
            "jupyter",
            "lite",
            "build",
            "--debug",
            *config,
            *contents,
            "--contents",
            os.path.join(app.srcdir, CONTENT_DIR),
            "--output-dir",
            os.path.join(app.outdir, JUPYTERLITE_DIR),
            "--apps",
            "lab",
            "--apps",
            "retro",
            "--apps",
            "repl",
            *voici_option,
            "--lite-dir",
            jupyterlite_dir,
        ]

        subprocess.run(command, cwd=app.srcdir, check=True)

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
    app.add_config_value("jupyterlite_dir", app.srcdir, rebuild="html")
    app.add_config_value("jupyterlite_contents", None, rebuild="html")
    app.add_config_value("jupyterlite_bind_ipynb_suffix", True, rebuild="html")

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

    # Initialize Voici directive
    app.add_node(
        VoiciIframe,
        html=(visit_element_html, None),
        latex=(skip, None),
        textinfo=(skip, None),
        text=(skip, None),
        man=(skip, None),
    )
    app.add_directive("voici", VoiciDirective)

    # CSS and JS assets
    copy_asset(str(HERE / "jupyterlite_sphinx.css"), str(Path(app.outdir) / "_static"))
    copy_asset(str(HERE / "jupyterlite_sphinx.js"), str(Path(app.outdir) / "_static"))

    app.add_css_file("https://fonts.googleapis.com/css?family=Vibur")
    app.add_css_file("jupyterlite_sphinx.css")

    app.add_js_file("jupyterlite_sphinx.js")
