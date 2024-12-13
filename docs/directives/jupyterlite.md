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

If you use the `:new_tab:` option in the directive, the Notebook will be opened in a new browser tab.
The tab will render the full-fledged Lab interface, which is more complete and showcases all features
of JupyterLite.

```rst
.. jupyterlite:: my_notebook.ipynb
   :new_tab: True
```

```{eval-rst}
.. jupyterlite:: my_notebook.ipynb
   :new_tab: True
```

The directive `search_params` allows to transfer some search parameters from the documentation URL to the Jupyterlite URL.\
Jupyterlite will then be able to fetch these parameters from its own URL.\
For example `:search_params: ["param1", "param2"]` will transfer the parameters *param1* and *param2*.
Use a boolean value to transfer all or none of the parameters (default to none): `:search_params: True`
