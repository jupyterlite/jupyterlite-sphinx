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

    for line in input_lines:
        line = line.strip()
        if line.startswith(">>>"):
            # This line is code
            # If there is any pending markdown text, add it to the notebook
            if md_lines:
                md_text = "\n".join(md_lines)
                md_text = _process_latex(md_text)

                nb.cells.append(new_markdown_cell(md_text))
                md_lines = []  # Reset markdown lines
            # Add this line to the code
            code_lines.append(line[4:])  # Remove '>>> ' prefix
        elif line.strip() == "" and code_lines:
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
    md_text = re.sub(r":math:`(?P<latex>.*?)`", r"$\g<latex>$", md_text)

    lines = md_text.split("\n")
    in_math_block = False
    wrapped_lines = []
    equation_lines = []

    for line in lines:
        stripped_line = line.strip()
        if stripped_line == ".. math::":
            in_math_block = True
            continue  # Skip the '.. math::' line

        if in_math_block:
            if stripped_line == "":
                if equation_lines:
                    # Join and wrap the equations, then reset
                    wrapped_lines.append(f"$$ {' '.join(equation_lines)} $$")
                    equation_lines = []
            elif line.startswith(" ") or line.startswith("\t"):
                equation_lines.append(stripped_line)
        else:
            wrapped_lines.append(line)

        # If you leave the indented block, the math block ends
        if in_math_block and not (line.startswith(" ") or line.startswith("\t")):
            in_math_block = False
            if equation_lines:
                wrapped_lines.append(f"$$ {' '.join(equation_lines)} $$")
            equation_lines = []

    return "\n".join(wrapped_lines)
