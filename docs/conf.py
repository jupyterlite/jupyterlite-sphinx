# -*- coding: utf-8 -*-

extensions = [
    'jupyterlite_sphinx',
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


