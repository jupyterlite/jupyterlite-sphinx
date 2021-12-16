import subprocess

from sphinx.application import Sphinx



def jupyterlite_build(app: Sphinx, error):
    print("[jupyterlite-sphinx] Running JupyterLite build")
    subprocess.call(["jupyter", "lite", "build", app.srcdir, app.outdir])


def setup(app):
    # print(dir(app))

    app.connect("config-inited", jupyterlite_build)
