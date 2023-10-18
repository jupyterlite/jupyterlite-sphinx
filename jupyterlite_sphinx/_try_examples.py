import nbformat as nbf
from nbformat.v4 import new_code_cell, new_markdown_cell
import re


def examples_to_notebook(input_lines):
    """Parse examples section of a docstring and convert to Jupyter notebook.

    Parameters
    ----------
    input_lines : iterable of str.
                  Lines within

    Returns
    -------
    dict
        json for a Jupyter Notebook

    Examples
    --------
    >>> from jupyterlite_sphinx.generate_notebook import examples_to_notebook

    >>> input_lines = [
    >>>            "Add two numbers. This block of text will appear as a\n",
    >>>            "markdown cell. The following block will become a code\n",
    >>>            "cell with the value 4 contained in the output.",
    >>>            "\n",
    >>>            ">>> x = 2\n",
    >>>            ">>> y = 2\n",
    >>>            ">>> x + y\n",
    >>>            "4\n",
    >>>            "\n",
    >>>            "Inline LaTeX like :math:`x + y = 4` will be converted\n",
    >>>            "correctly within markdown cells. As will block LaTeX\n",
    >>>            "such as\n",
    >>>            "\n",
    >>>            ".. math::\n",
    >>>            "\n",
    >>>            "    x = 2,\;y = 2
    >>>            "\n",
    >>>            "    x + y = 4\n",
    >>>          ]
    >>> notebook = examples_to_notebook(input_lines)
    """
    nb = nbf.v4.new_notebook()

    code_lines = []
    md_lines = []
    output_line = None
    inside_multiline_code_block = False


    for line in input_lines:
        line = line.rstrip("\n")
        if line.startswith(">>>"):
            if inside_multiline_code_block:
                # End of a multiline code block.
                inside_multiline_code_block = False

            # This line is code
            # If there is any pending markdown text, add it to the notebook
            if md_lines:
                md_text = "\n".join(md_lines)
                md_text = _process_latex(md_text)

                nb.cells.append(new_markdown_cell(md_text))
                md_lines = []  # Reset markdown lines
            # Add this line to the code
            code_lines.append(line[4:])  # Remove '>>> ' prefix
        elif line.startswith("...") and code_lines:
            # This is a continuation of a multiline code block.
            inside_multiline_code_block = True
            code_lines.append(line[4:])
        elif line.rstrip("\n") == "" and code_lines:
            # This line is blank, so it is the end of a code cell
            # If there is any pending code, add it to the notebook
            code_text = "\n".join(code_lines)
            cell = new_code_cell(code_text)
            if output_line is not None:
                cell.outputs.append(
                    nbf.v4.new_output(
                        output_type="execute_result", data={"text/plain": output_line}
                    ),
                )
                output_line = None
            nb.cells.append(cell)
            code_lines = []  # Reset code lines
        elif code_lines:
            # This line is the output of the previous code cell
            output_line = line
        else:
            # This line is markdown
            md_lines.append(line)

    # If there is any pending markdown or code, add it to the notebook
    if md_lines:
        md_text = "\n".join(md_lines)
        md_text = _process_latex(md_text)

        # Convert blocks of LaTeX equations
        md_text = _process_latex(md_text)

        nb.cells.append(new_markdown_cell(md_text))
    if code_lines:
        code_text = "\n".join(code_lines)
        cell = new_code_cell(code_text)
        if output_line is not None:
            cell.outputs.append(
                nbf.v4.new_output(
                    output_type="execute_result", data={"text/plain": output_line}
                ),
            )
        nb.cells.append(cell)
    return nb


def _process_latex(md_text):
    # Map rst latex directive to $ so latex renders in notebook.
    md_text = re.sub(r":math:\s*`(?P<latex>.*?)`", r"$\g<latex>$", md_text)

    lines = md_text.split("\n")
    in_math_block = False
    wrapped_lines = []
    equation_lines = []

    for line in lines:
        if line.strip() == ".. math::":
            in_math_block = True
            continue  # Skip the '.. math::' line

        if in_math_block:
            if line.strip() == "":
                if equation_lines:
                    # Join and wrap the equations, then reset
                    wrapped_lines.append(f"$$ {' '.join(equation_lines)} $$")
                    equation_lines = []
            elif line.startswith(" ") or line.startswith("\t"):
                equation_lines.append(line.strip())
        else:
            wrapped_lines.append(line)

        # If you leave the indented block, the math block ends
        if in_math_block and not (
            line.startswith(" ") or line.startswith("\t") or line.strip() == ""
        ):
            in_math_block = False
            if equation_lines:
                wrapped_lines.append(f"$$ {' '.join(equation_lines)} $$")
            equation_lines = []

    return "\n".join(wrapped_lines)


# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#docstring-sections
_non_example_docstring_section_headers = (
    "Args",
    "Arguments",
    "Attention",
    "Attributes",
    "Caution",
    "Danger",
    "Error",
    "Hint",
    "Important",
    "Keyword Args",
    "Keyword Arguments",
    "Methods",
    "Note",
    "Notes",
    "Other Parameters",
    "Parameters",
    "Return",
    "Returns",
    "Raise",
    "Raises",
    "References",
    "See Also",
    "Tip",
    "Todo",
    "Warning",
    "Warnings",
    "Warns",
    "Yield",
    "Yields",
)


_examples_start_pattern = re.compile(r".. (rubric|admonition):: Examples")
_next_section_pattern = re.compile(
    "|".join(
        [
            rf".. (rubric|admonition)::\s*{header}"
            for header in _non_example_docstring_section_headers
        ]
        # If examples section is last, processed by numpydoc may appear at end.
        + [r"^\.\. \!\! processed by numpydoc \!\!"]
    )
)


def insert_try_examples_directive(lines, **options):
    """Adds try_examples directive to Examples section of a docstring.

    Hack to allow for a config option to enable try_examples functionality
    in all Examples sections (unless a comment "..! disable_try_examples" is
    added explicitly after the section header.)


    Parameters
    ----------
    docstring : list of str
        Lines of a docstring at time of "autodoc-process-docstring", with section
        headers denoted by `.. rubric::` or `.. admonition::`.


    Returns
    -------
    list of str
        Updated version of the input docstring which has a try_examples directive
        inserted in the Examples section (if one exists) with all Examples content
        indented beneath it. Does nothing if the comment "..! disable_try_examples"
        is included at the top of the Examples section. Also a no-op if the
        try_examples directive is already included.
    """
    # Search for the "Examples" section start
    for left_index, line in enumerate(lines):
        if _examples_start_pattern.search(line):
            break
    else:
        # No examples section found
        return lines[:]
    # Increment to the line after "Examples"
    left_index += 1
    # Skip empty lines to get to the first content line after "Examples"
    while left_index < len(lines) and not lines[left_index].strip():
        left_index += 1
    # If reached the end of the docstring without finding non-empty line
    if left_index == len(lines):
        return lines[:]
    # Check for the "..! disable_try_examples" directive
    if lines[left_index].strip() == "..! disable_try_examples::":
        return lines[:]
    # Check if the ".. try_examples::" directive already exists
    if ".. try_examples::" == lines[left_index].strip():
        return lines[:]
    # Find the end of the Examples section
    right_index = left_index
    while right_index < len(lines) and not _next_section_pattern.search(
        lines[right_index]
    ):
        right_index += 1

    # Add the ".. try_examples::" directive and indent the content of the Examples section
    new_lines = (
        lines[:left_index]
        + [".. try_examples::"]
        + [f"    :{key}: {value}" for key, value in options.items()]
        + [""]
        + ["    " + line for line in lines[left_index:right_index]]
        + [""]
        + lines[right_index:]
    )

    return new_lines
