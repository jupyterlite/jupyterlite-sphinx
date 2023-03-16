# -*- coding: utf-8 -*-
import shutil

from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent


extensions = [
    'jupyterlite_sphinx',
    'myst_parser',
]

html_theme = "pydata_sphinx_theme"
html_logo = "_static/icon.svg"

jupyterlite_config = "jupyter_lite_config.json"
jupyterlite_contents = "./custom_contents"
jupyterlite_bind_ipynb_suffix = False

master_doc = 'index'

# General information about the project.
project = 'JupyterLite Sphinx extension'

# theme configuration 
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/jupyterlite/jupyterlite-sphinx",
            "icon": "fa-brands fa-github",
        }
    ]
}

# Copy the markdown file here
shutil.copy(ROOT / "CHANGELOG.md", HERE / "changelog.md")
