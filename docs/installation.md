# Installation

You can install `jupyterlite-sphinx` with `pip`:

```
pip install jupyterlite-sphinx
```

then you need to add the `jupyterlite-sphinx` extension to your `conf.py` file of your sphinx docs:

```python
extensions = [
    'jupyterlite_sphinx',
    # And other sphinx extensions
    # ...
]
```

JupyterLite should automatically show up in your built online documentation. To preview it locally, you can navigate to the build directory (e.g. `_build/html`) and use `python -m http.server` to serve the site.
