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

In order to have Python packages pre-installed in the kernel environment, you can use [jupyterlite-xeus](https://jupyterlite-xeus.readthedocs.io), with the `xeus-python` kernel.

You would need `jupyterlite-xeus` installed in your docs build environment.

You can pre-install packages by adding an `environment.yml` file in the docs directory, with `xeus-python` defined as one of the dependencies. It will pre-build the environment when running the `jupyter lite build`.

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

### Suppressing jupyterlite logging

`jupyterlite` can produce large amounts of output to the terminal when docs are building.
By default, this output is silenced, but will still be printed if the invocation of
`jupyterlite build` fails. To unsilence this output, set

```python
jupyterlite_silence = False
```

in your Sphinx `conf.py`.

## Additional CLI arguments for `jupyter lite build`

Additional arguments can be passed to the `jupyter lite build` command using the configuration
option `jupyterlite_build_command_options` in `conf.py`. The following example shows how to
specify an alternative location for the `xeus` kernel's `environment.yml` file as discussed
[here](https://github.com/jupyterlite/xeus#usage).

```python
jupyterlite_build_command_options = {
    "XeusAddon.environment_file": "jupyterlite_environment.yml",
    }
```

This causes the additional option `--XeusAddon.environment_file=jupyterlite_environment.yml`
to be passed to `jupyter lite build` internally within `jupyterlite-sphinx`. Note that one
does not include the leading dashes, `--`, in the keys.

The options `--contents`, `--output-dir`, and `--lite-dir` cannot be passed to `jupyter lite build` in this way.
These can instead be set with
the [`jupyterlite_contents`](#jupyterlite-content) and the[`jupyterlite_dir`](#jupyterlite-dir) configuration
options described above.
