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
            self, rawsource="", *children, replite_options=None, **attributes
            ):
        super().__init__("", replite_options=replite_options)

    def html(self):
        replite_options = self["replite_options"]
        options = '&'.join(
            [f'{key}={value}' for key, value in replite_options.items()]
        )

        return (
            f'<iframe src="{JUPYTERLITE_DIR}/repl/index.html?{options}"'
            'width="100%" height="100%"></iframe>'
        )


class RepliteDirective(Directive):
    """The ``.. replite::`` directive.

    Adds a replite console to the docs.
    """

    has_content = True
    required_arguments = 0
    option_spec = {
        'kernel': directives.unchanged,
        'toolbar': directives.unchanged,
        'theme': directives.unchanged,
    }

    def run(self):
        replite_options = {**self.options}

        if self.content:
            replite_options["code"] = ''.join(self.content)

        return [RepliteIframe(replite_options=replite_options)]


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
