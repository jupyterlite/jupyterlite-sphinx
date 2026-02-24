# Configuration

JupyterLite-sphinx can be configured in your `conf.py` file by setting some global Python variables:

## JupyterLite content

You can embed custom content (notebooks and data files) in your JupyterLite build by providing the following config:

```python
jupyterlite_contents = ["./path/to/my/notebooks/", "my_other_notebook.ipynb"]
```

`jupyterlite_contents` can be a string or a list of strings. Each string is expanded using the Python `glob.glob` function with its recursive option. See the [glob documentation](https://docs.python.org/3/library/glob.html#glob.glob) and the [wildcard pattern documentation](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch) for more details. This option supports both paths relative to the docs source directory and absolute ones.

### Ignoring content

You can exclude some contents from your specified contents, for example:

```python
jupyterlite_contents = ["./path/to/my/contents"]
jupyterlite_ignore_contents = [r".*\.txt"]
```

`jupyterlite_ignore_contents` can be a string or a list of strings. Strings are used as Python regular expressions to match and exclude files from your custom content. It's best to use raw string literals for your ignore strings, otherwise you'll need to double-escape (in other words, `r".*\.txt"` is more readable than `".*\\.txt"`).

Each string is passed directly to [the JupyterLite build `--ignore-contents` CLI argument](https://jupyterlite.readthedocs.io/en/stable/reference/cli.html#common-parameters).

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

You can provide [custom configuration files](https://jupyterlite.readthedocs.io/en/stable/howto/configure/config_files.html)
to your JupyterLite deployment for build-time configuration and settings overrides.

The build-time configuration can be used to change the default settings for JupyterLite, such
as changing which assets are included, the locations of the assets, which plugins are enabled,
and more.

The runtime configuration can be used to change the settings of the JupyterLite deployment
after it has been built, such as changing the theme, the default kernel, the default language,
and more.

<!-- TODO: Run-time configuration via `jupyter-lite.json` not added yet here
because I can't yet find a direct jupyter lite CLI mapping for that option -->

```python
# Build-time configuration for JupyterLite
jupyterlite_config = "jupyter_lite_config.json"
# Override plugins and extension settings
jupyterlite_overrides = "overrides.json"
```

## Setting default button texts for the `JupyterLite`, `NotebookLite`, `Replite`, and `Voici` directives

When using the `:new_tab:` option in the `JupyterLite`, `NotebookLite`, `Replite`, and `Voici` directives,
the button text defaults to "Open as a notebook", "Open in a REPL", and "Open with Voici", respectively.

You can optionally the button text on a global level for these directives by setting the
following values in your `conf.py` file:

```python
jupyterlite_new_tab_button_text = "My custom JupyterLite button text"
notebooklite_new_tab_button_text = "My custom NotebookLite button text"
replite_new_tab_button_text = "My custom Replite button text"
voici_new_tab_button_text = "My custom Voici button text"
```

You can override this text on a per-directive basis by passing the `:new_tab_button_text:` option
to the directive. Note that this is compatible only if `:new_tab:` is also provided.

## REPL configuration options

We provide several configuration options for the Replite directive that control the behaviour and appearance of the REPL. These options can be set globally in `conf.py` and then overridden on a per-directive basis.

### REPL code auto-execution

```python
# enable or disable automatic code execution when the REPL loads
# (available in jupyterlite-core 0.5.0 and later)
replite_auto_execute = True  # default is True
```

This setting controls whether code snippets in REPL environments automatically execute when loaded. Set to `False` to disable automatic execution. You can override this on a per-directive basis with `:execute: True` or `:execute: False`.

### REPL interface customisations (JupyterLite 0.6.0 and later)

The following options customise how the REPL interface behaves and is presented:

```python
# clear previous cells when a new cell is executed
replite_clear_cells_on_execute = False  # default is False

# clear the code content in the prompt cell after execution
replite_clear_code_content_on_execute = False  # default is False

# hide input cells, showing only output
replite_hide_code_input = False  # default is False

# position of the prompt cell ('bottom', 'top', 'left', or 'right')
replite_prompt_cell_position = "bottom"  # default is "bottom"

# show or hide the kernel banner
replite_show_banner = True  # default is True
```

These global settings can be overridden in individual directives using the corresponding options:

- `:clear_cells_on_execute: True/False`
- `:clear_code_content_on_execute: True/False`
- `:hide_code_input: True/False`
- `:prompt_cell_position: bottom/top/left/right`
- `:show_banner: True/False`

For more details and visual examples of each, see the [Replite directive documentation](directives/replite.md).

## Strip particular tagged cells from IPython Notebooks

When using the `NotebookLite`, `JupyterLite`, or `Voici` directives with a notebook passed to them, you can
strip particular tagged cells from the notebook before rendering it in the JupyterLite console.

This behaviour can be enabled by setting the following config:

```python
strip_tagged_cells = True
```

and then by tagging the cells you want to strip with the `jupyterlite_sphinx_strip` tag in the JSON metadata
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
Sphinx-specific content. It can be used to remove either code cells or Markdown cells.

For example, you can use this feature to remove the `toctree` directive from the rendered notebook
in the JupyterLite console:

````json
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
````

where the cell with the `toctree` directive will be removed from the rendered notebook in
the JupyterLite console.

In the case of a MyST notebook, you can use the following syntax to tag the cells:

````markdown

+++ {"tags": ["jupyterlite_sphinx_strip"]}

# Heading 1

This is a Markdown cell that will be stripped from the rendered notebook in the
JupyterLite console.

+++

```{code-cell} ipython3
:tags: [jupyterlite_sphinx_strip]

# This is a code cell that will be stripped from the rendered notebook in the
# JupyterLite console.
def foo():
    print(3)
```

```{code-cell} ipython3
# This cell will not be stripped
def bar():
    print(4)
```
````

The Markdown cells are not wrapped, and hence the `+++` and `+++` markers are used to
indicate where the cells start and end. For more details around writing and customising
MyST-flavoured notebooks, please refer to the
[MyST Markdown overview](https://jupyterbook.org/en/stable/content/myst.html).

Note that this feature is only available for the `NotebookLite`, `JupyterLite`, and the
`Voici` directives and works with the `.md` (MyST) or `.ipynb` files passed to them. It
is not implemented for the `TryExamples` directive.

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
