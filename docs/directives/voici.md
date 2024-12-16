# Voici directive

`jupyterlite-sphinx` provides a `voici` directive that allows you to embed a [voici dashboard](https://github.com/voila-dashboards/voici) in your docs.

```rst
.. voici::
   :height: 600px
```

```{eval-rst}
.. voici::
   :height: 600px
```

You can provide a notebook file (either Jupyter-based or MyST-Markdown flavoured) that will be
rendered with Voici:

1. Jupyter Notebook

```rst
.. voici:: my_notebook.ipynb
   :height: 600px
   :prompt: Try Voici!
   :prompt_color: #dc3545
```

```{eval-rst}
.. voici:: my_notebook.ipynb
   :height: 600px
   :prompt: Try Voici!
   :prompt_color: #dc3545
```

2. MyST Markdown

```rst
.. voici:: my_markdown_notebook.md
   :height: 600px
   :prompt: Try Voici!
   :prompt_color: `#dc3545`
```

```{eval-rst}
.. voici:: my_markdown_notebook.md
   :height: 600px
   :prompt: Try Voici!
   :prompt_color: `#dc3545`
```

If you use the `:new_tab:` option in the directive, the Voici dashboard will execute and render
the notebook in a new browser tab, instead of in the current page.

```rst
.. voici:: my_notebook.ipynb
   :new_tab: True
```

```{eval-rst}
.. voici:: my_notebook.ipynb
   :new_tab: True
```

When using this option, it is also possible to customise the button text, overriding the
global value using an additional `:button_text:` parameter:

```rst
.. voici:: my_notebook.ipynb
   :new_tab: True
   :button_text: My custom Voici button text
```

```{eval-rst}
.. voici:: my_notebook.ipynb
   :new_tab: True
   :button_text: My custom Voici button text
```
