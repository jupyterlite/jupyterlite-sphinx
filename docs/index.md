# jupyterlite-sphinx

A Sphinx extension that provides utilities for embedding JupyterLite in your docs.

`jupyterlite-sphinx` brings the power of JupyterLite to your Sphinx documentation. It makes a full JupyterLite deployment in your docs and provide some utilities for using that deployment easily.

```{eval-rst}
.. replite::
   :kernel: xeus-python
   :toolbar: 0
   :theme: JupyterLab Light
   :width: 100%
   :height: 600px

   print("Hello from a JupyterLite console!")
```

```{toctree}
:maxdepth: 2

installation
configuration
```

## Usage

`jupyterlite-sphinx` provides a collection of directives that allows you to embed the different JupyterLite UIs directly in your documentation page.
Each of those directives can be configured with the following options:

- `width` (default `"100%"`) the width of the UI
- `height` (default `"600px"`) the height of the UI
- `theme` (default `None`) the JupyterLab theme to use
- `prompt` (default `False`) whether or not to lazy-load the UI. If the value is a string, it will use this value for the prompt button.
- `prompt_color` (default `#f7dc1e`) The color of the prompt button, if there is one.

```{toctree}
:maxdepth: 2

directives/jupyterlite
directives/retrolite
directives/replite
full
changelog
```
