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

If you use the `:new_tab:` option in the directive, the Notebook will be opened in a new browser tab.
The tab will render the classic Notebook UI, which is more minimal and does not showcase the entire
Lab interface.

```rst
.. notebooklite:: my_notebook.ipynb
   :new_tab: True
```

```{eval-rst}
.. notebooklite:: my_notebook.ipynb
   :new_tab: True
```

When using this option, it is also possible to customise the button text, overriding the
global value using an additional `:new_tab_button_text:` parameter:

```rst
.. notebooklite:: my_notebook.ipynb
   :new_tab: True
   :new_tab_button_text: My custom NotebookLite button text
```

```{eval-rst}
.. notebooklite:: my_notebook.ipynb
   :new_tab: True
   :new_tab_button_text: My custom NotebookLite button text
```
