# -*- coding: utf-8 -*-

extensions = [
    "sphinx.ext.mathjax",
    "jupyterlite_sphinx",
    "myst_parser",
]

myst_enable_extensions = [
    "colon_fence"
]

html_theme = "pydata_sphinx_theme"
html_logo = "_static/icon.svg"

jupyterlite_contents = "./custom_contents"
jupyterlite_bind_ipynb_suffix = False

master_doc = "index"

# General information about the project.
project = "JupyterLite Sphinx extension"

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

html_static_path = ["_static"]
html_css_files = ["try_examples.css"]

suppress_warnings = ["myst.xref_missing"]
