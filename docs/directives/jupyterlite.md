# JupyterLite directive

`jupyterlite-sphinx` provides a `jupyterlite` directive that allows you to embed JupyterLab in your docs.

```rst
.. jupyterlite::
   :width: 100%
   :height: 600px
   :prompt: Try JupyterLite!
   :prompt_color: #00aa42
```

```{eval-rst}
.. jupyterlite::
   :width: 100%
   :height: 600px
   :prompt: Try JupyterLite!
   :prompt_color: #00aa42
```

You can also pass a Notebook file to open automatically:

```rst
.. jupyterlite:: my_notebook.ipynb
   :width: 100%
   :height: 600px
   :prompt: Try JupyterLite!
   :prompt_color: #00aa42
```

```{eval-rst}
.. jupyterlite:: my_notebook.ipynb
   :width: 100%
   :height: 600px
   :prompt: Try JupyterLite!
   :prompt_color: #00aa42
```
