# RetroLite directive

`jupyterlite-sphinx` provides a `retrolite` directive that allows you to embed Retrolab in your docs.

```rst
.. retrolite::
   :width: 100%
   :height: 600px
   :prompt: Try Retrolite!
```

```{eval-rst}
.. retrolite::
   :width: 100%
   :height: 600px
   :prompt: Try Retrolite!
```

You can also pass a Notebook file to open:

```rst
.. retrolite:: my_notebook.ipynb
   :width: 100%
   :height: 600px
   :prompt: Try Retrolite!
```

```{eval-rst}
.. retrolite:: my_notebook.ipynb
   :width: 100%
   :height: 600px
   :prompt: Try Retrolite!
```
