# TryExamples directive

`jupyterlite-sphinx` provides the experimental `try_examples` directive which allows
docstring examples sections written in [doctestformat](https://docs.python.org/3/library/doctest.html) to be swapped with an embedded classic Notebook at the push of a button.


```rst
Examples
--------
.. try_examples::
    :button_css:
        background-color: #f7dc1e;
	border: none;
    	padding: 5px 10px;
   	border-radius: 15px;
	font-family: vibur;
	font-size: x-large;
	box-shadow: 0 2px 5px rgba(108,108,108,0.2);
    :button_hover_css:
        background-color: #fff221;
 	transform: scale(1.02);
	box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
	cursor: pointer;
    :button_horizontal_position: right
    :button_vertical_position: top
    :button_text: Try it in a classic notebook!
    :min_height: 200px


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

        \int_{x=-\infty}^{\infty}e^{-x^2}\mathrm{d}x = \sqrt{\pi}

    If you are displaying `math output <https://www.sphinx-doc.org/en/master/usage/extensions/math.html>`_
    with sphinx.
```


```{eval-rst}
Examples
--------
.. try_examples::
    :button_css:
        background-color: #f7dc1e;
	border: none;
    	padding: 5px 10px;
   	border-radius: 15px;
	font-family: vibur;
	font-size: x-large;
	box-shadow: 0 2px 5px rgba(108,108,108,0.2);
    :button_hover_css:
        background-color: #fff221;
 	transform: scale(1.02);
	box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
	cursor: pointer;
    :button_horizontal_position: right
    :button_vertical_position: top
    :button_text: Try it in a classic notebook!
    :min_height: 200px

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
    with sphinx.
```

## Configuration

The button's text, position, and style can be configured to match your page design. The
text can be configured with the option `:button_text:`. The options `:button_css:` and
`:button_hover_css:` take lists of css properties as in the example above, and
apply them to the button. `:button_horizontal_position:` can be one of `left`, `right`, or
`center` and `:button_vertical_position:` can be one of `top` or `bottom`. The position
is with respect to the rendered examples block / embedded notebook
(depending on which is active).

The height of the embedded notebook's iframe container is calculated to match the height
of the rendered doctest examples so that it takes up the same amount of space on the
page. The `:min_height:` option can be used to ensure that the embedded notebook will not
be unuseably small for very short examples blocks, though its use can cause the contents
of the page to shift when the button is pressed.

the `:theme:` option available for other `jupyterlite-sphinx` directives is also
available.

If you are using [sphinx.ext.autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html) with [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html) or [sphinx.ext.napoleon](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html), you
can set the option

```python
global_enable_try_examples = True
```

in your sphinx `conf.py` in order to automatically insert the `try_examples` directive
in examples sections during the `"autodoc-process-docstring"` event. Configuration values
can be set globally for the inserted `try_examples` directives by setting the config values
`try_examples_global_button_css`, etc. as below. All valid config values are supported
by prepending `try_examples_global_`.

```python
global_enable_try_examples = True
try_examples_global_button_css = """
color: white;
background-color: #0054a6;
border: none;
padding: 5px 10px;
border-radius: 5px;
cursor: pointer;
"""
try_examples_global_button_hover_css = """
background-color: #0066cc;
transform: scale(1.02);
box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
"""

try_examples_global_button_text = "Try it in your browser!"
try_examples_global_min_height = "200px"
```

If an examples section already contains a `try_examples` directive, no additional
directives will be inserted, allowing for specific cases to be separately configured
if needed. Adding the comment `..! disable_try_examples` as the first non-empty line under
the section header for an examples section will prevent a directive from being inserted,
allowing for specification of examples sections which should not be made interactive.

## Other considerations
If you are using the `TryExamples` directive in your documentation, you'll need to ensure
that the version of the package installed in the Jupyterlite kernel you are using
matches that of the version you are documenting.
