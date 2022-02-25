import os
import shutil

from pathlib import Path

import subprocess

from docutils.parsers.rst import directives
from docutils.nodes import SkipNode, Element
from docutils.parsers import rst

from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective


JUPYTERLITE_DIR = "lite"


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
        width=None,
        height=None,
        replite_options=None,
        **attributes,
    ):
        super().__init__(
            "", width=width, height=height, replite_options=replite_options
        )

    def html(self):
        replite_options = self["replite_options"]
        options = "&".join([f"{key}={value}" for key, value in replite_options.items()])

        width = self["width"] if self["width"] is not None else "100%"
        height = self["height"] if self["height"] is not None else "100%"

        return (
            f'<iframe src="{JUPYTERLITE_DIR}/repl/index.html?{options}"'
            f'width="{width}" height="{height}"></iframe>'
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
        width = self.options.pop("width", None)
        height = self.options.pop("height", None)

        if self.content:
            self.options["code"] = "".join(self.content)

        return [RepliteIframe(width=width, height=height, replite_options=self.options)]


class RetroliteIframe(Element):
    """Appended to the doctree by the RetroliteDirective directive

    Renders an iframe that shows a Notebook with RetroLite.
    """

    def __init__(self, rawsource="", *children, notebook=None, **attributes):
        super().__init__("", notebook=notebook)

    def html(self):
        notebook = self["notebook"]

        return (
            f'<iframe src="{JUPYTERLITE_DIR}/retro/notebooks/?path={notebook}"'
            'width="100%" height=1000px></iframe>'
        )


class RetroliteDirective(SphinxDirective):
    """The ``.. retrolite::`` directive.

    Renders a Notebook with RetroLite in the docs.
    """

    has_content = False
    required_arguments = 1
    option_spec = {}

    def run(self):
        notebook = self.arguments[0]
        notebook_name = os.path.basename(notebook)

        notebooks_dir = (
            Path(self.env.app.outdir)
            / JUPYTERLITE_DIR
            / "retro"
            / "notebooks"
            / notebook_name
        )

        # Copy the Notebook for RetroLite to find
        shutil.copyfile(notebook, str(notebooks_dir))

        return [RetroliteIframe(notebook=notebook_name)]


class RetroLiteParser(rst.Parser):
    """Sphinx source parser for Jupyter notebooks.

    Shows the Notebook using retrolite."""

    supported = ("jupyterlite_notebook",)

    def parse(self, inputstring, document):
        title = os.path.splitext(os.path.basename(document.current_source))[0]
        super().parse(
            f"{title}\n{'=' * len(title)}\n.. retrolite:: {document.current_source}",
            document,
        )


def jupyterlite_build(app: Sphinx, error):
    print("[jupyterlite-sphinx] Running JupyterLite build")
    subprocess.call(
        [
            "jupyter",
            "lite",
            "init",
            "--output-dir",
            os.path.join(app.outdir, JUPYTERLITE_DIR),
        ]
    )

    # Cleanup
    try:
        os.remove(".jupyterlite.doit.db")
    except FileNotFoundError:
        pass


def setup(app):
    # Build the JupyterLite output
    app.connect("config-inited", jupyterlite_build)

    # Initialize RetroLite directive and parser
    app.add_node(
        RetroliteIframe,
        html=(visit_element_html, None),
        latex=(skip, None),
        textinfo=(skip, None),
        text=(skip, None),
        man=(skip, None),
    )
    app.add_directive("retrolite", RetroliteDirective)

    app.add_source_parser(RetroLiteParser)
    app.add_source_suffix(".ipynb", "jupyterlite_notebook")

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
