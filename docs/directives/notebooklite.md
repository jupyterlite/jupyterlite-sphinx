# NotebookLite directive

`jupyterlite-sphinx` provides a `notebooklite` directive that allows you to embed the classic Notebook UI in your docs.

```rst
.. notebooklite::
   :width: 100%
   :height: 600px
   :prompt: Try classic Notebook!
```

```{eval-rst}
.. notebooklite::
   :width: 100%
   :height: 600px
   :prompt: Try classic Notebook!
```

You can also pass a Notebook file to open:

```rst
.. notebooklite:: my_notebook.ipynb
   :width: 100%
   :height: 600px
   :prompt: Try classic Notebook!
```

```{eval-rst}
.. notebooklite:: my_notebook.ipynb
   :width: 100%
   :height: 600px
   :prompt: Try classic Notebook!
```
