import os

import subprocess

from sphinx.application import Sphinx


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
    app.connect("config-inited", jupyterlite_build)
