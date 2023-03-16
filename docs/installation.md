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

````{note}
By default `jupyterlite-sphinx` does not install a Python kernel.
If you would like have a Python kernel available in your docs you can install either `jupyterlite-pyodide-kernel` or `jupyterlite-xeus-python` with `pip`:

```shell
# to install the Python kernel based on Pyodide
pip install jupyterlite-pyodide-kernel

# to install the Python kernel based on Xeus Python
pip install jupyterlite-xeus-python
```
````