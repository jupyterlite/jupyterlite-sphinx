import os
import json
from uuid import uuid4
import shutil
import tempfile
from warnings import warn
import glob
import re
import nbformat as nbf

from pathlib import Path

from urllib.parse import quote

import subprocess

from docutils.parsers.rst import directives
from docutils.nodes import SkipNode, Element
from docutils import nodes

from sphinx.application import Sphinx
from sphinx.ext.doctest import DoctestDirective
from sphinx.util.docutils import SphinxDirective
from sphinx.util.fileutil import copy_asset
from sphinx.parsers import RSTParser

from ._try_examples import examples_to_notebook, insert_try_examples_directive

try:
    import voici
except ImportError:
    voici = None

HERE = Path(__file__).parent

CONTENT_DIR = "_contents"
JUPYTERLITE_DIR = "lite"


# Used for nodes that do not need to be rendered
def skip(self, node):
    raise SkipNode


# Used to render an element node as HTML
def visit_element_html(self, node):
    self.body.append(node.html())
    raise SkipNode


class _PromptedIframe(Element):
    def __init__(
        self,
        rawsource="",
        *children,
        iframe_src="",
        width="100%",
        height="100%",
        prompt=False,
        prompt_color=None,
        search_params="false",
        **attributes,
    ):
        super().__init__(
            "",
            iframe_src=iframe_src,
            width=width,
            height=height,
            prompt=prompt,
            prompt_color=prompt_color,
            search_params=search_params,
        )

    def html(self):
        iframe_src = self["iframe_src"]
        search_params = self["search_params"]

        if self["prompt"]:
            prompt = (
                self["prompt"] if isinstance(self["prompt"], str) else "Try It Live!"
            )
            prompt_color = (
                self["prompt_color"] if self["prompt_color"] is not None else "#f7dc1e"
            )

            placeholder_id = uuid4()
            container_style = f'width: {self["width"]}; height: {self["height"]};'

            return f"""
                <div
                    class=\"jupyterlite_sphinx_iframe_container\"
                    style=\"{container_style}\"
                    onclick=\"window.jupyterliteShowIframe(
                        '{placeholder_id}',
                        window.jupyterliteConcatSearchParams('{iframe_src}', {search_params})
                    )\"
                >
                    <div
                        id={placeholder_id}
                        class=\"jupyterlite_sphinx_try_it_button jupyterlite_sphinx_try_it_button_unclicked\"
                        style=\"background-color: {prompt_color};\"
                    >
                    {prompt}
                    </div>
                </div>
            """

        return (
            f'<iframe src="{iframe_src}"'
            f'width="{self["width"]}" height="{self["height"]}" class="jupyterlite_sphinx_raw_iframe"></iframe>'
        )


class _LiteIframe(_PromptedIframe):
    def __init__(
        self,
        rawsource="",
        *children,
        prefix=JUPYTERLITE_DIR,
        content=[],
        notebook=None,
        lite_options={},
        **attributes,
    ):
        if content:
            code_lines = ["" if not line.strip() else line for line in content]
            code = "\n".join(code_lines)

            lite_options["code"] = code

        app_path = self.lite_app
        if notebook is not None:
            lite_options["path"] = notebook
            app_path = f"{self.lite_app}{self.notebooks_path}"

        options = "&".join(
            [f"{key}={quote(value)}" for key, value in lite_options.items()]
        )

        iframe_src = f'{prefix}/{app_path}{f"?{options}" if options else ""}'

        super().__init__(rawsource, *children, iframe_src=iframe_src, **attributes)


class RepliteIframe(_LiteIframe):
    """Appended to the doctree by the RepliteDirective directive

    Renders an iframe that shows a repl with JupyterLite.
    """

    lite_app = "repl/index.html"
    notebooks_path = ""


class JupyterLiteIframe(_LiteIframe):
    """Appended to the doctree by the JupyterliteDirective directive

    Renders an iframe that shows a Notebook with JupyterLite.
    """

    lite_app = "lab/"
    notebooks_path = ""


class NotebookLiteIframe(_LiteIframe):
    """Appended to the doctree by the NotebookliteDirective directive

    Renders an iframe that shows a Notebook with NotebookLite.
    """

    lite_app = "tree/"
    notebooks_path = "../notebooks/"


class VoiciIframe(_PromptedIframe):
    """Appended to the doctree by the VoiciDirective directive

    Renders an iframe that shows a Notebook with Voici.
    """

    def __init__(
        self,
        rawsource="",
        *children,
        prefix=JUPYTERLITE_DIR,
        notebook=None,
        lite_options={},
        **attributes,
    ):
        if notebook is not None:
            app_path = f"voici/render/{notebook.replace('.ipynb', '.html')}"
        else:
            app_path = "voici/tree"

        options = "&".join(
            [f"{key}={quote(value)}" for key, value in lite_options.items()]
        )

        iframe_src = f'{prefix}/{app_path}{f"?{options}" if options else ""}'

        super().__init__(rawsource, *children, iframe_src=iframe_src, **attributes)


class RepliteDirective(SphinxDirective):
    """The ``.. replite::`` directive.

    Adds a replite console to the docs.
    """

    has_content = True
    required_arguments = 0
    option_spec = {
        "width": directives.unchanged,
        "height": directives.unchanged,
        "kernel": directives.unchanged,
        "toolbar": directives.unchanged,
        "theme": directives.unchanged,
        "prompt": directives.unchanged,
        "prompt_color": directives.unchanged,
        "search_params": directives.unchanged,
    }

    def run(self):
        width = self.options.pop("width", "100%")
        height = self.options.pop("height", "100%")

        prompt = self.options.pop("prompt", False)
        prompt_color = self.options.pop("prompt_color", None)

        search_params = search_params_parser(self.options.pop("search_params", False))

        prefix = os.path.relpath(
            os.path.join(self.env.app.srcdir, JUPYTERLITE_DIR),
            os.path.dirname(self.get_source_info()[0]),
        )

        return [
            RepliteIframe(
                prefix=prefix,
                width=width,
                height=height,
                prompt=prompt,
                prompt_color=prompt_color,
                content=self.content,
                search_params=search_params,
                lite_options=self.options,
            )
        ]


class _LiteDirective(SphinxDirective):
    has_content = False
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        "width": directives.unchanged,
        "height": directives.unchanged,
        "theme": directives.unchanged,
        "prompt": directives.unchanged,
        "prompt_color": directives.unchanged,
        "search_params": directives.unchanged,
    }

    def run(self):
        width = self.options.pop("width", "100%")
        height = self.options.pop("height", "1000px")

        prompt = self.options.pop("prompt", False)
        prompt_color = self.options.pop("prompt_color", None)

        search_params = search_params_parser(self.options.pop("search_params", False))

        source_location = os.path.dirname(self.get_source_info()[0])

        prefix = os.path.relpath(
            os.path.join(self.env.app.srcdir, JUPYTERLITE_DIR), source_location
        )

        if self.arguments:
            # As with other directives like literalinclude, an absolute path is
            # assumed to be relative to the document root, and a relative path
            # is assumed to be relative to the source file
            rel_filename, notebook = self.env.relfn2path(self.arguments[0])
            self.env.note_dependency(rel_filename)

            notebook_name = os.path.basename(notebook)

            notebooks_dir = Path(self.env.app.srcdir) / CONTENT_DIR / notebook_name

            # Copy the Notebook for NotebookLite to find
            os.makedirs(os.path.dirname(notebooks_dir), exist_ok=True)
            try:
                shutil.copyfile(notebook, str(notebooks_dir))
            except shutil.SameFileError:
                pass
        else:
            notebook_name = None

        return [
            self.iframe_cls(
                prefix=prefix,
                notebook=notebook_name,
                width=width,
                height=height,
                prompt=prompt,
                prompt_color=prompt_color,
                search_params=search_params,
                lite_options=self.options,
            )
        ]


class JupyterLiteDirective(_LiteDirective):
    """The ``.. jupyterlite::`` directive.

    Renders a Notebook with JupyterLite in the docs.
    """

    iframe_cls = JupyterLiteIframe


class NotebookLiteDirective(_LiteDirective):
    """The ``.. notebooklite::`` directive.

    Renders a Notebook with NotebookLite in the docs.
    """

    iframe_cls = NotebookLiteIframe


class VoiciDirective(_LiteDirective):
    """The ``.. voici::`` directive.

    Renders a Notebook with Voici in the docs.
    """

    iframe_cls = VoiciIframe

    def run(self):
        if voici is None:
            raise RuntimeError(
                "Voici must be installed if you want to make use of the voici directive: pip install voici"
            )

        return super().run()


class NotebookLiteParser(RSTParser):
    """Sphinx source parser for Jupyter notebooks.

    Shows the Notebook using notebooklite."""

    supported = ("jupyterlite_notebook",)

    def parse(self, inputstring, document):
        title = os.path.splitext(os.path.basename(document.current_source))[0]
        # Make the "absolute" filename relative to the source root
        filename = "/" + os.path.relpath(document.current_source, self.env.app.srcdir)
        super().parse(
            f"{title}\n{'=' * len(title)}\n.. notebooklite:: {filename}",
            document,
        )


class TryExamplesDirective(SphinxDirective):
    """Add button to try doctest examples in Jupyterlite notebook."""

    has_content = True
    required_arguments = 0
    option_spec = {
        "theme": directives.unchanged,
        "button_text": directives.unchanged,
        "button_css": directives.unchanged,
        "button_hover_css": directives.unchanged,
        "button_horizontal_position": directives.unchanged,
        "button_vertical_position": directives.unchanged,
        "min_height": directives.unchanged,
    }

    def run(self):
        if "generated_notebooks" not in self.env.temp_data:
            self.env.temp_data["generated_notebooks"] = {}

        directive_key = f"{self.env.docname}-{self.lineno}"
        notebook_unique_name = self.env.temp_data["generated_notebooks"].get(
            directive_key
        )

        button_text = self.options.pop("button_text", "Try it with Jupyterlite!")
        button_css = self.options.pop("button_css", "")
        button_hover_css = self.options.pop("button_hover_css", "")
        button_horizontal_position = self.options.pop(
            "button_horizontal_position", "right"
        )
        button_vertical_position = self.options.pop("button_vertical_position", "top")
        min_height = self.options.pop("min_height", "200px")

        if button_horizontal_position not in ["left", "center", "right"]:
            raise RuntimeError(
                "try_examples directive expects button_horizontal_position to be one of"
                f" 'left', 'center', or 'right', received {button_horizontal_position}."
            )

        if button_vertical_position not in ["bottom", "top"]:
            raise RuntimeError(
                "try_examples directive expects button_vertical_position to be one of"
                f" 'top' or 'bottom', received {button_vertical_position}."
            )

        # We need to get the relative path back to the documentation root from
        # whichever file the docstring content is in.
        docname = self.env.docname
        depth = len(docname.split("/")) - 1
        relative_path_to_root = "/".join([".."] * depth)
        prefix = os.path.join(relative_path_to_root, JUPYTERLITE_DIR)

        lite_app = "tree/"
        notebooks_path = "../notebooks/"

        content_container_node = nodes.container(
            classes=["try_examples_outer_container"]
        )
        examples_div_id = uuid4()
        content_container_node["ids"].append(examples_div_id)
        # Parse the original content to create nodes
        content_node = nodes.container()
        content_node["classes"].append("try_examples_content")
        self.state.nested_parse(self.content, self.content_offset, content_node)

        if notebook_unique_name is None:
            nb = examples_to_notebook(self.content)
            self.content = None
            notebooks_dir = Path(self.env.app.srcdir) / CONTENT_DIR
            notebook_unique_name = f"{uuid4()}.ipynb".replace("-", "_")
            self.env.temp_data["generated_notebooks"][
                directive_key
            ] = notebook_unique_name
            # Copy the Notebook for NotebookLite to find
            os.makedirs(notebooks_dir, exist_ok=True)
            with open(notebooks_dir / Path(notebook_unique_name), "w") as f:
                # nbf.write incorrectly formats multiline arrays in output.
                json.dump(nb, f, indent=4, ensure_ascii=False)

        self.options["path"] = notebook_unique_name
        app_path = f"{lite_app}{notebooks_path}"
        options = "&".join(
            [f"{key}={quote(value)}" for key, value in self.options.items()]
        )

        iframe_parent_div_id = uuid4()
        iframe_div_id = uuid4()
        iframe_src = f'{prefix}/{app_path}{f"?{options}" if options else ""}'

        # Parent container (initially hidden)
        iframe_parent_container_div_start = (
            f'<div id="{iframe_parent_div_id}" '
            f'class="try_examples_outer_container hidden">'
        )

        iframe_parent_container_div_end = "</div>"
        iframe_container_div = (
            f'<div id="{iframe_div_id}" '
            f'class="try_examples_iframe_container">'
            f"</div>"
        )

        # Button with the onclick event to swap embedded notebook back to examples.
        go_back_button_html = (
            '<div class="try_examples_button_container">'
            '<button class="try_examples_button" '
            f"onclick=\"window.tryExamplesHideIframe('{examples_div_id}',"
            f"'{iframe_parent_div_id}')\">"
            "Go Back</button>"
            "</div>"
        )

        # Button with the onclick event to swap examples with embedded notebook.
        try_it_button_html = (
            '<div class="try_examples_button_container">'
            '<button class="try_examples_button" '
            f"onclick=\"window.tryExamplesShowIframe('{examples_div_id}',"
            f"'{iframe_div_id}','{iframe_parent_div_id}','{iframe_src}',"
            f"'{min_height}')\">"
            f"{button_text}</button>"
            "</div>"
        )
        try_it_button_node = nodes.raw("", try_it_button_html, format="html")

        # Combine everything
        if button_vertical_position == "top":
            notebook_container_html = (
                iframe_parent_container_div_start
                + go_back_button_html
                + iframe_container_div
                + iframe_parent_container_div_end
            )
            content_container_node += try_it_button_node
            content_container_node += content_node
        else:
            notebook_container_html = (
                iframe_parent_container_div_start
                + iframe_container_div
                + go_back_button_html
                + iframe_parent_container_div_end
            )
            content_container_node += content_node
            content_container_node += try_it_button_node

        notebook_container = nodes.raw("", notebook_container_html, format="html")

        # Generate css for button based on options.
        if button_css:
            button_css = f".try_examples_button {{{button_css}}}"
        if button_hover_css:
            button_hover_css = f".try_examples_button:hover {{{button_hover_css}}}"

        justify = {"left": "flex-start", "center": "center", "right": "flex-end"}[
            button_horizontal_position
        ]

        button_container_css = (
            ".try_examples_button_container {"
            f"display: flex; justify-content: {justify}"
            "}"
        )

        complete_button_css = button_css + button_hover_css + button_container_css

        style_tag = nodes.raw(
            "", f"<style>{complete_button_css}</style>", format="html"
        )

        return [content_container_node, notebook_container, style_tag]


def _process_docstring_examples(app, docname, source):
    source_path = app.env.doc2path(docname)
    if source_path.endswith(".py"):
        source[0] = insert_try_examples_directive(source[0])


def _process_autodoc_docstrings(app, what, name, obj, options, lines):
    try_examples_options = {
        "theme": app.config.try_examples_global_theme,
        "button_text": app.config.try_examples_global_button_text,
        "button_css": app.config.try_examples_global_button_css,
        "button_hover_css": app.config.try_examples_global_button_hover_css,
        "button_horizontal_position": app.config.try_examples_global_button_horizontal_position,
        "button_vertical_position": app.config.try_examples_global_button_vertical_position,
        "min_height": app.config.try_examples_global_min_height,
    }
    try_examples_options = {
        key: value for key, value in try_examples_options.items() if value is not None
    }
    modified_lines = insert_try_examples_directive(lines, **try_examples_options)
    lines.clear()
    lines.extend(modified_lines)


def conditional_process_examples(app, config):
    if config.global_enable_try_examples:
        app.connect("source-read", _process_docstring_examples)
        app.connect("autodoc-process-docstring", _process_autodoc_docstrings)


def inited(app: Sphinx, config):
    # Create the content dir
    os.makedirs(os.path.join(app.srcdir, CONTENT_DIR), exist_ok=True)

    if (
        config.jupyterlite_bind_ipynb_suffix
        and ".ipynb" not in config.source_suffix
        and ".ipynb" not in app.registry.source_suffix
    ):
        app.add_source_suffix(".ipynb", "jupyterlite_notebook")


def jupyterlite_build(app: Sphinx, error):
    if error is not None:
        # Do not build JupyterLite
        return

    if app.builder.format == "html":
        print("[jupyterlite-sphinx] Running JupyterLite build")
        jupyterlite_config = app.env.config.jupyterlite_config
        jupyterlite_contents = app.env.config.jupyterlite_contents
        jupyterlite_dir = app.env.config.jupyterlite_dir

        config = []
        if jupyterlite_config:
            config = ["--config", jupyterlite_config]

        if jupyterlite_contents is None:
            jupyterlite_contents = []
        elif isinstance(jupyterlite_contents, str):
            jupyterlite_contents = [jupyterlite_contents]

        # Expand globs in the contents strings
        jupyterlite_contents = [
            match
            for pattern in jupyterlite_contents
            for match in glob.glob(pattern, recursive=True)
        ]

        contents = []
        for content in jupyterlite_contents:
            contents.extend(["--contents", content])

        apps_option = []
        for liteapp in ["notebooks", "edit", "lab", "repl", "tree", "consoles"]:
            apps_option.extend(["--apps", liteapp])
        if voici is not None:
            apps_option.extend(["--apps", "voici"])

        command = [
            "jupyter",
            "lite",
            "build",
            "--debug",
            *config,
            *contents,
            "--contents",
            os.path.join(app.srcdir, CONTENT_DIR),
            "--output-dir",
            os.path.join(app.outdir, JUPYTERLITE_DIR),
            *apps_option,
            "--lite-dir",
            jupyterlite_dir,
        ]

        subprocess.run(command, cwd=app.srcdir, check=True)

        print("[jupyterlite-sphinx] JupyterLite build done")

    # Cleanup
    try:
        shutil.rmtree(os.path.join(app.srcdir, CONTENT_DIR))
        os.remove(".jupyterlite.doit.db")
    except FileNotFoundError:
        pass


def setup(app):
    # Initialize NotebookLite parser
    app.add_source_parser(NotebookLiteParser)

    app.connect("config-inited", inited)
    # We need to build JupyterLite at the end, when all the content was created
    app.connect("build-finished", jupyterlite_build)

    # Config options
    app.add_config_value("jupyterlite_config", None, rebuild="html")
    app.add_config_value("jupyterlite_dir", app.srcdir, rebuild="html")
    app.add_config_value("jupyterlite_contents", None, rebuild="html")
    app.add_config_value("jupyterlite_bind_ipynb_suffix", True, rebuild="html")

    app.add_config_value("global_enable_try_examples", default=False, rebuild=True)
    app.add_config_value("try_examples_global_theme", default=None, rebuild=True)
    app.add_config_value("try_examples_global_button_css", default=None, rebuild="html")
    app.add_config_value(
        "try_examples_global_button_hover_css", default=None, rebuild="html"
    )
    app.add_config_value(
        "try_examples_global_button_horizontal_position", default=None, rebuild="html"
    )
    app.add_config_value(
        "try_examples_global_button_vertical_position", default=None, rebuild="html"
    )
    app.add_config_value("try_examples_global_min_height", default=None, rebuild="html")
    app.add_config_value(
        "try_examples_global_button_text",
        default=None,
        rebuild="html",
    )

    # Initialize NotebookLite and JupyterLite directives
    app.add_node(
        NotebookLiteIframe,
        html=(visit_element_html, None),
        latex=(skip, None),
        textinfo=(skip, None),
        text=(skip, None),
        man=(skip, None),
    )
    app.add_directive("notebooklite", NotebookLiteDirective)
    # For backward compatibility
    app.add_directive("retrolite", NotebookLiteDirective)
    app.add_node(
        JupyterLiteIframe,
        html=(visit_element_html, None),
        latex=(skip, None),
        textinfo=(skip, None),
        text=(skip, None),
        man=(skip, None),
    )
    app.add_directive("jupyterlite", JupyterLiteDirective)

    # Initialize Replite directive
    app.add_node(
        RepliteIframe,
        html=(visit_element_html, None),
        latex=(skip, None),
        textinfo=(skip, None),
        text=(skip, None),
        man=(skip, None),
    )
    app.add_directive("replite", RepliteDirective)

    # Initialize Voici directive
    app.add_node(
        VoiciIframe,
        html=(visit_element_html, None),
        latex=(skip, None),
        textinfo=(skip, None),
        text=(skip, None),
        man=(skip, None),
    )
    app.add_directive("voici", VoiciDirective)

    # Initialize TryExamples directive
    app.add_directive("try_examples", TryExamplesDirective)
    app.connect("config-inited", conditional_process_examples)

    # CSS and JS assets
    copy_asset(str(HERE / "jupyterlite_sphinx.css"), str(Path(app.outdir) / "_static"))
    copy_asset(str(HERE / "jupyterlite_sphinx.js"), str(Path(app.outdir) / "_static"))

    app.add_css_file("https://fonts.googleapis.com/css?family=Vibur")
    app.add_css_file("jupyterlite_sphinx.css")

    app.add_js_file("jupyterlite_sphinx.js")


def search_params_parser(search_params: str) -> str:
    pattern = re.compile(r"^\[(?:\s*[\"']{1}([^=\s\,&=\?\/]+)[\"']{1}\s*\,?)+\]$")
    if not search_params:
        return "false"
    if search_params in ["True", "False"]:
        return search_params.lower()
    elif pattern.match(search_params):
        return search_params.replace('"', "'")
    else:
        raise ValueError(
            'The search_params directive must be either True, False or ["param1", "param2"].\n'
            'The params name shouldn\'t contain any of the following characters ["\\", "\'", """, ",", "?", "=", "&", " ").'
        )
