# Fullscreen access

Once and JupyterLite example has been activate by a user, and "Open in Tab" button is available that will open the same
JupyterLite instance in a separate tab.

## custom link to JupyterLite

You can access the JupyterLite deployment that `jupyterlite-sphinx` made for you, in fullscreen, following the `./lite/lab` and `./lite/retro` relative urls:

```{eval-rst}

- `JupyterLab <lite/lab/index.html>`_
- `Notebook <lite/tree/index.html>`_

```

If you want to open a specific notebook in fullscreen JupyterLab/Notebook, you can use the `path` URL parameter, e.g. `./lite/lab/index.html?path=my_noteboook.ipynb`.
