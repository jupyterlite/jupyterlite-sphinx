# Configuration

JupyterLite-sphinx can be configured in your `conf.py` file by setting some global Python variables:

## JupyterLite content

You can embed custom content (notebooks and data files) in your JupyterLite build by providing the following config:

```python
jupyterlite_contents = ["./path/to/my/notebooks/", "my_other_notebook.ipynb"]
```

`jupyterlite_contents` can be a string or a list of strings. Each string is expanded using the Python `glob.glob` function with its recursive option. See the [glob documentation](https://docs.python.org/3/library/glob.html#glob.glob) and the [wildcard pattern documentation](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch) for more details.

## JupyterLite dir

By default, jupyterlite-sphinx runs the `jupyter lite build` command in a temporary directory, you can overwrite this behavior and ask jupyterlite to build in a given directory:

```python
# Build in the current directory
jupyterlite_dir = "."
```

This allows for jupyterlite to automatically pick-up some paths <https://jupyterlite.readthedocs.io/en/latest/reference/cli.html#the-lite-dir>

## JupyterLite config

You can provide [custom configuration](https://jupyterlite.readthedocs.io/en/latest/howto/index.html#configuring-a-jupyterlite-deployment)
to your JupyterLite deployment.

For example, if you want to have bqplot working in this deployment, you need to install the bqplot federated extension
and you can serve the bqplot wheel to `piplite`, this is done by telling your `conf.py` where to look for the jupyterlite config:

```python
jupyterlite_config = "jupyterlite_config.json"
```

The `jupyterlite_config.json` containing the following:

```json
{
    "LiteBuildConfig": {
        "federated_extensions": [
            "https://conda.anaconda.org/conda-forge/noarch/bqplot-0.12.33-pyhd8ed1ab_0.tar.bz2",
        ],
        "ignore_sys_prefix": true
    }
    "PipliteAddon": {
        "piplite_urls": [
            "https://files.pythonhosted.org/packages/py2.py3/b/bqplot/bqplot-0.12.33-py2.py3-none-any.whl",
        ]
    }
}
```

Then you should be able to show Notebooks working with bqplot!

```rst
.. retrolite:: bqplot.ipynb
```

```{eval-rst}
.. retrolite:: bqplot.ipynb
```

## Disable the `.ipynb` docs source binding

By default, jupyterlite-sphinx binds the `.ipynb` source suffix so that it renders Notebooks included in the doctree with JupyterLite.
This is known to bring warnings with plugins like sphinx-gallery, or to conflict with nbsphinx.

You can disable this behavior by setting the following config:

```python
jupyterlite_bind_ipynb_suffix = False
```
