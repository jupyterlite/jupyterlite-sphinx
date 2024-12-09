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

You can provide a notebook (either Jupyter-based or MyST-Markdown flavoured) to open:

1. Jupyter Notebook

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

2. MyST Markdown

```rst
.. notebooklite:: my_notebook.md
   :width: 100%
   :height: 600px
   :prompt: Try classic Notebook!
```

```{eval-rst}
.. notebooklite:: my_notebook.md
   :width: 100%
   :height: 600px
   :prompt: Try classic Notebook!
```
