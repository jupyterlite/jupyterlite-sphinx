# Configuration

JupyterLite-sphinx can be configured in your `conf.py` file by setting some global Python variables:

## JupyterLite content

You can embed custom content (notebooks and data files) in your JupyterLite build by providing the following config:

```python
jupyterlite_contents = ["./path/to/my/notebooks/", "my_other_notebook.ipynb"]
```

`jupyterlite_contents` can be a string or a list of strings. Each string is expanded using the Python `glob.glob` function with its recursive option. See the [glob documentation](https://docs.python.org/3/library/glob.html#glob.glob) and the [wildcard pattern documentation](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch) for more details.

## JupyterLite dir

By default, jupyterlite-sphinx runs the `jupyter lite build` command in the docs directory, you can overwrite this behavior and ask jupyterlite to build in a given directory:

```python
# Build in the current directory
jupyterlite_dir = "/path/to/your/lite/dir"
```

## Pre-installed packages

In order to have Python packages pre-installed in the kernel environment, you can use [jupyterlite-xeus-python](https://xeus-python-kernel.readthedocs.io).

You would need `jupyterlite-xeus-python` installed in your docs build environment.

You can pre-install packages by adding an `environment.yml` file in the docs directory, this file will be found automatically by xeus-python which will pre-build the environment when running the jupyter lite build.

Furthermore, this automatically installs any labextension that it founds, for example installing ipyleaflet will make ipyleaflet work without the need to manually install the jupyter-leaflet labextension.

Say you want to install NumPy, Matplotlib and ipycanvas, it can be done by creating the environment.yml file with the following content:

```yaml
name: xeus-python-kernel
channels:
  - https://repo.mamba.pm/emscripten-forge
  - https://repo.mamba.pm/conda-forge
dependencies:
  - numpy
  - matplotlib
  - ipycanvas
```

## JupyterLite config

You can provide [custom configuration](https://jupyterlite.readthedocs.io/en/latest/howto/index.html#configuring-a-jupyterlite-deployment)
to your JupyterLite deployment.

```python
jupyterlite_config = "jupyterlite_config.json"
```

## Disable the `.ipynb` docs source binding

By default, jupyterlite-sphinx binds the `.ipynb` source suffix so that it renders Notebooks included in the doctree with JupyterLite.
This is known to bring warnings with plugins like sphinx-gallery, or to conflict with nbsphinx.

You can disable this behavior by setting the following config:

```python
jupyterlite_bind_ipynb_suffix = False
```
