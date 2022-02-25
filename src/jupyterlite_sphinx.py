import os

import subprocess

from docutils.parsers.rst import Directive
from docutils.nodes import SkipNode, Element

from sphinx.application import Sphinx


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
        # replite_options = self["replite_options"]
        return (
            '<iframe src="lite/repl/index.html" width="100%" height="100%"></iframe>'
        )


class RepliteDirective(Directive):

    def run(self):
        print('state_machine', self.state_machine)
        print('content', self.content)
        print('arguments', self.arguments)
        # TODO Extract replite options from arguments?
        return [RepliteIframe(replite_options={})]


def jupyterlite_build(app: Sphinx, error):
    print("[jupyterlite-sphinx] Running JupyterLite build")
    subprocess.call([
        "jupyter", "lite", "init",
        "--output-dir", os.path.join(app.outdir, 'lite')
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
