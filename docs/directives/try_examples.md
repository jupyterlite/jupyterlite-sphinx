# TryExamples directive

`jupyterlite-sphinx` provides the experimental `try_examples` directive which allows
docstring examples sections written in [doctest format](https://docs.python.org/3/library/doctest.html) to be swapped with an embedded classic Notebook at the push of a button.

Below is an example of the directive in use. The button has been styled with custom
css as explained in the configuration section below. Without custom css, the button will
be plain and unadorned.

Note that as starting JupyterLite can download a significant amount of data, and
that the Jupyter interface is not optimized for mobile, the buttons will be
hidden on mobile by default (screen width 480px or smaller). This can be
changed by overwriting with custom CSS.


```rst
Examples
--------
.. try_examples::

    Doctest examples sections are parsed and converted to notebooks. Blocks of text
    like this become markdown cells. Codeblocks begin with ``>>>``. Contiguous blocks
    of code are combined into a single code cell.

    >>> x = 2
    >>> y = 2
    >>> x + y
    4

    ``...`` is used to continue multiline statements.

    >>> def f(x, y):
    ...     return x + y
    >>> f(2, 2)
    4

    Inline LaTeX like :math:`x + y = 4` is converted, as is block LaTeX like

    .. math::

        \int_{x=-\infty}^{\infty}e^{-x^2}\mathrm{d}x = \sqrt{\pi}

    If you are displaying `math output <https://www.sphinx-doc.org/en/master/usage/extensions/math.html>`_
    with sphinx. Sphinx links such as the one in the previous sentence are also converted to
    markdown format.
```

and here is how this looks and works when rendered.


```{eval-rst}
Examples
--------
.. try_examples::

    Doctest examples sections are parsed and converted to notebooks. Blocks of text
    like this become markdown cells. Codeblocks begin with `>>>`. Contiguous blocks
    of code are combined into a single code cell.

    >>> x = 2
    >>> y = 2
    >>> x + y
    4

    `...` is used to continue multiline statements.

    >>> def f(x, y):
    ...     return x + y
    >>> f(2, 2)
    4

    Inline LaTeX like :math:`x + y = 4` is converted, as is block LaTeX like

    .. math::

        \int_{-\infty}^{\infty}e^{-x^2}\mathrm{d}x = \sqrt{\pi}

    If you are displaying `math output <https://www.sphinx-doc.org/en/master/usage/extensions/math.html>`_
    with sphinx. Sphinx links such as the one in the previous sentence are also converted to
    markdown format.
```

By default, the height of the embedded notebook's iframe container is calculated to match the height of the rendered doctest examples so that it takes up the same amount of space on the
page.

## Configuration

The position and style of the button can be customized to match your documentation's
design by adding custom css as explained in Sphinx's documentation [here](https://docs.readthedocs.io/en/stable/guides/adding-custom-css.html#how-to-add-custom-css-or-javascript-to-sphinx-documentation). The buttons have class `try_examples_button`. The buttons are placed within
containers with class `try_examples_button_container`, which can be selected to adjust the
positioning of the button. The css for the example above is

```css

.try_examples_button {
    color: white;
    background-color: #0054a6;
    border: none;
    padding: 5px 10px;
    border-radius: 10px;
    margin-bottom: 5px;
    box-shadow: 0 2px 5px rgba(108,108,108,0.2);
}

.try_examples_button:hover {
    background-color: #0066cc;
    transform: scale(1.02);
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    cursor: pointer;
}

.try_examples_button_container {
    display: flex;
    justify-content: flex-end;
}
```


The `try_examples` directive has options
* `:height:` To set a specific value for the height of the [iframe](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe) containing the embedded notebook.
* `:button_text` To customize the text of the button that replaces the rendered examples with an embedded notebook.
* `:theme:` This works the same as for the other JupyterLite-Sphinx directives.
* `:example_class:` An html class to attach to the outer container for the rendered
examples content and embedded notebook. This can be used in a custom css file to allow
for more precise customization, eg. different button styles across different examples.
* `:warning_text:` Prepend a markdown cell to the notebook containing this text, styled to make it clear this is intended as a warning.

Here's an example with some options set

```rst
.. try_examples::
    :button_text: Try it in your browser!
    :height: 400px
    :example_class: blue-bottom
    :warning_text: Interactive examples are experimental and may not always work as expected.

    The button text has changed and the height now exceeds the size of the content.

    >>> x = 2
    >>> y = 2
    >>> x + y
    4

    We've also added the ``blue-bottom`` class, the button should appear as blue,
    below the examples, and on the left side of the screen.

    See `try_examples.css <https://github.com/jupyterlite/jupyterlite-sphinx/blob/main/docs/_static/try_examples.css>`_
    to see how we achieved this via custom css.
```

and here is the result

```{eval-rst}
.. try_examples::
    :button_text: Try it in your browser!
    :height: 400px
    :example_class: blue-bottom
    :warning_text: Interactive examples are experimental and may not always work as expected.

    The button text has changed and the height now exceeds the size of the content.

    >>> x = 2
    >>> y = 2
    >>> x + y
    4

    We've also added the ``blue-bottom`` class, the button should appear as blue,
    below the examples, and on the left side of the screen.

    See `try_examples.css <https://github.com/jupyterlite/jupyterlite-sphinx/blob/main/docs/_static/try_examples.css>`_
    to see how we achieved this via custom css.
```


### Global Configuration

For projects with a large number of existing doctest examples, it would be tedious to add
the `try_examples` directive manually to each docstring example. If you are using [sphinx.ext.autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html) with either [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html) or [sphinx.ext.napoleon](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html), you
can set the option.

```python
global_enable_try_examples = True
```

in your sphinx `conf.py` in order to automatically insert the `try_examples` directive
in examples sections during the `"autodoc-process-docstring"` event. This works by
identifying section headings. An examples section includes all of the content beneath
an examples heading, and up to either the next heading or the end of the docstring if
there are no further headings. One of  `numpydoc` or `sphinx.ext.napoleon` is required
because these map the section headers to a standardized format.

If an examples section already contains a `try_examples` directive, no additional
directives will be inserted, allowing for specific cases to be separately configured
if needed. Adding the comment


```rst
.. disable_try_examples
```

as the first non-empty line under
the section header for an examples section will prevent a directive from being inserted,
allowing for specification of examples sections which should not be made interactive.


The button text, theme, and warning text can be set globally with the config variables
`try_examples_global_button_text`, `try_examples_global_theme`, and `try_examples_global_warning_text` in `conf.py`;
these apply both to automatically and manually inserted directives. Options set explicitly in a directive will
override the global configuration.

```python
global_enable_try_examples = True
try_examples_global_button_text = "Try it in your browser!"
try_examples_global_height = "200px"
try_examples_global_warning_text = "Interactive examples are experimental and may not always work as expected."
```

There is no option to set a global specific height because the proper height
should depend on the size of the examples content. Again, the default height of
the embedded notebook's iframe container matches the height of the associated
rendered doctest example so that it takes up the same amount of space on the
page. For very small examples this may lead to an unusably small notebook. It's possible
to set a global minimum height in the `try_examples.json` configuration file described
below.

### try_examples.json configuration file.

Users may place a configuration file `try_examples.json` in the source root of
their documentation. This configuration file will be copied to the build root of
the deployed documentation. Changes to the configuration file in the build root
will be respected without rebuilding the documentation, allowing for runtime
configuration.

The current options are

#### "ignore_patterns"

The format is a list of
[JavaScript Regex patterns](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions) attached to the key `"ignore_patterns"` like below.

```json
{
    "ignore_patterns": ["^\/latest/.*", "^\/stable\/reference\/generated\/example.html"]
}
```

`TryExamples` buttons will be hidden in url pathnames matching at least one of these
patterns, effectively disabling the interactive documentation. In the provided example:

* The pattern `"^\/latest\/.*"` disables interactive examples for urls for the documentation
  for the latest version of the package, which may be useful if this documentation is
  for a development version for which a corresponding package build is not available
  in a JupyterLite kernel.

* The pattern `"^\/stable\/reference\/generated\/example.html"` targets a particular url
  in the documentation for the latest stable release.

Note that these patterns should match the [pathname](https://developer.mozilla.org/en-US/docs/Web/API/Location/pathname) of the url, not the full url. This is the path portion of
the url. For instance, the pathname of https://jupyterlite-sphinx.readthedocs.io/en/latest/directives/try_examples.html is `/en/latest/directives/try_examples.html`. Also, note that since these are JavaScript-based regular
expressions, to use special characters in the regular expression (such as `/`), they
must be escaped with a backslash (`\`).

Again, the configuration file can be added or edited within the deployed documentation,
allowing for disabling or enabling examples without rebuilding the documentation.

#### "global_min_height"

To avoid having unusably small notebooks for very small examples due to the default of
having the embedded notebooks' iframe containers take the same amount of space as the
rendered content they replace, users can set a global minimum height in
`try_examples.json`.

```json
{
    "global_min_height": "400px"
}
```

This allows the minimum height to be set or changed without rebuilding the docs. This
configuration value will be ignored when a specific height is supplied as an option to
`.. try_examples::`.


## Other considerations
If you are using the `TryExamples` directive in your documentation, you'll need to ensure
that the version of the package installed in the Jupyterlite kernel you are using
matches that of the version you are documenting.
