import os

import subprocess

from docutils.parsers.rst import directives, Directive
from docutils.nodes import SkipNode, Element

from sphinx.application import Sphinx


JUPYTERLITE_DIR = 'lite'


# Used for nodes that do not need to be rendered
def skip(self, node):
    raise SkipNode


# Used to render an element node as HTML
def visit_element_html(self, node):
    self.body.append(node.html())
    raise SkipNode


class RepliteIframe(Element):
    """Appended to the doctree by the RepliteDirective directive

    Renders an iframe that points shows a replite console.
    """

    def __init__(
            self, rawsource="", *children, width=None, height=None,
            replite_options=None, **attributes
            ):
        super().__init__(
            "", width=width, height=height, replite_options=replite_options)

    def html(self):
        replite_options = self["replite_options"]
        options = '&'.join(
            [f'{key}={value}' for key, value in replite_options.items()]
        )

        width = self["width"] if self["width"] is not None else "100%"
        height = self["height"] if self["height"] is not None else "100%"

        return (
            f'<iframe src="{JUPYTERLITE_DIR}/repl/index.html?{options}"'
            f'width="{width}" height="{height}"></iframe>'
        )


class RepliteDirective(Directive):
    """The ``.. replite::`` directive.

    Adds a replite console to the docs.
    """

    has_content = True
    required_arguments = 0
    option_spec = {
        'width': directives.unchanged,
        'height': directives.unchanged,
        'kernel': directives.unchanged,
        'toolbar': directives.unchanged,
        'theme': directives.unchanged,
    }

    def run(self):
        width = self.options.pop('width', None)
        height = self.options.pop('height', None)

        if self.content:
            self.options["code"] = ''.join(self.content)

        return [
            RepliteIframe(
                width=width, height=height, replite_options=self.options
            )
        ]


def jupyterlite_build(app: Sphinx, error):
    print("[jupyterlite-sphinx] Running JupyterLite build")
    subprocess.call([
        "jupyter", "lite", "init",
        "--output-dir", os.path.join(app.outdir, JUPYTERLITE_DIR)
    ])

    # Cleanup
    try:
        os.remove('.jupyterlite.doit.db')
    except FileNotFoundError:
        pass


def setup(app):
    # Build the JupyterLite output
    app.connect("config-inited", jupyterlite_build)

    # Initialize Replite directive
    app.add_node(
        RepliteIframe,
        html=(visit_element_html, None),
        latex=(skip, None),
        textinfo=(skip, None),
        text=(skip, None),
        man=(skip, None),
    )
    app.add_directive('replite', RepliteDirective)
