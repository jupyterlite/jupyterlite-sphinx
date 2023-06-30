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

You can provide a notebook that will be rendered with Voici:

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
