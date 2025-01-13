# Fullscreen access

Once a JupyterLite example gets activated by a user, an "Open in Tab" button becomes available, which will open the same
JupyterLite instance in a separate tab.

## Custom links to JupyterLite apps

You can access the JupyterLite app that `jupyterlite-sphinx` made for you, in fullscreen, using the following links:

- [JupyterLab](lite/lab/index.html)
- [Notebook](lite/tree/index.html)
- [REPL](lite/repl/index.html)
- [Voici](lite/voici/index.html)

## Tips for handling URLs

If you want to open a specific notebook in fullscreen JupyterLab/Notebook/Voici, you can use the `path` URL parameter, e.g. 

- `./lite/lab/index.html?path=my_noteboook.ipynb` for Lab
- `./lite/notebooks/index.html?path=my_notebook.ipynb` for Notebook
- `./lite/voici/render/my_notebook.html` for Voici

If you want to add code to the REPL for execution, you can use the `code` URL parameter, e.g. `./lite/repl/index.html?code=print("Hello, world!")`. You may also use `&execute=0` to prevent the code from being executed until you press Enter.
More configuration options are available with the [REPL documentation](https://jupyterlite.readthedocs.io/en/stable/quickstart/embed-repl.html#configuration)

Please see the documentation individual options and global [Configuration](configuration.md) options for more information.
