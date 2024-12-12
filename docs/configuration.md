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

Furthermore, this automatically installs any labextension that it finds, for example, installing `ipyleaflet` will make `ipyleaflet` work without the need to manually install the `jupyter-leaflet` labextension.

Say you want to install NumPy, Matplotlib and ipycanvas, it can be done by creating an `environment.yml` file with the following content:

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

## JupyterLite configuration

You can provide [custom configuration files](https://jupyterlite.readthedocs.io/en/latest/howto/configure/config_files.html)
to your JupyterLite deployment for build-time configuration and settings overrides.

<!-- TODO: Run-time configuration via `jupyter-lite.json` not added yet here
because I can't yet find a direct jupyter lite CLI mapping for that option -->

```python
# Build-time configuration for JupyterLite
jupyterlite_config = "jupyter_lite_config.json"
# Override plugins and extension settings
jupyterlite_overrides = "overrides.json"
```

## Strip particular tagged cells from IPython Notebooks

When using the `NotebookLite`, `JupyterLite`, or `Voici` directives with a notebook passed to them, you can
strip particular tagged cells from the notebook before rendering it in the JupyterLite console.

This behaviour can be enabled by setting the following config:

```python
strip_tagged_cells = True
```

and then by tagging the cells you want to strip with the tag `jupyterlite_sphinx_strip` in the JSON metadata
of the cell, like this:

```json
"metadata": {
  "tags": [
    "jupyterlite_sphinx_strip"
  ]
}
```

This is useful when you want to remove some cells from the rendered notebook in the JupyterLite
console, for example, cells that are used for adding reST-based directives or other
Sphinx-specific content.

For example, you can use this feature to remove the `toctree` directive from the rendered notebook
in the JupyterLite console:

```json
{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "tags": [
          "jupyterlite_sphinx_strip"
        ]
      },
      "source": [
        "# Table of Contents\n",
        "\n",
        "```{toctree}\n",
        ":maxdepth: 2\n",
        "\n",
        "directives/jupyterlite\n",
        "directives/notebooklite\n",
        "directives/replite\n",
        "directives/voici\n",
        "directives/try_examples\n",
        "full\n",
        "changelog\n",
        "```"
      ]
    }
  ]
}
```

where the cell with the `toctree` directive will be removed from the rendered notebook in
the JupyterLite console.

Note that this feature is only available for the `NotebookLite`, `JupyterLite`, and the
`Voici` directives and works with the `.ipynb` files passed to them. It is not implemented
for the `TryExamples` directive.

## Disable the `.ipynb` docs source binding

By default, jupyterlite-sphinx binds the `.ipynb` source suffix so that it renders Notebooks included in the doctree with JupyterLite.
This is known to bring warnings with plugins like `sphinx-gallery`, or to conflict with `nbsphinx`.

You can disable this behavior by setting the following config:

```python
jupyterlite_bind_ipynb_suffix = False
```

### Suppressing JupyterLite logging

`jupyterlite` can produce large amounts of output to the terminal when docs are building.
By default, this output is silenced, but will still be printed if the invocation of
`jupyter lite build` fails. To unsilence this output, set

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

This is an advanced feature and users are responsible for providing sensible command line options.
The standard precedence rules between `jupyter lite build` CLI options and other means of configuration apply.
See the [jupyter lite CLI](https://jupyterlite.readthedocs.io/en/latest/reference/cli.html) documentation
for more info.
