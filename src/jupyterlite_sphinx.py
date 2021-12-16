from docutils.parsers import Parser


class JupyterLiteParser(Parser):
    supported = ('notebook',)

    def parse(self, inputstring, document):
        print(dir(self))

        print(document)


def setup(app):
    print(dir(app))

    app.add_source_suffix('.ipynb', 'notebook')
    app.add_source_parser(JupyterLiteParser)
