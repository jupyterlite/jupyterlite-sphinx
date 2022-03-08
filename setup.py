from setuptools import setup


setup(
    name='jupyterlite-sphinx',
    version='0.4.0',
    package_dir={'': 'src'},
    py_modules=['jupyterlite_sphinx'],
    python_requires='>=3.7',
    install_requires=[
        'docutils',
        'jupyterlite',
        'sphinx>=1.8',
        'jupyter_server',
        'jupyterlab_server',
    ],
    author='JupyterLite Contributors',
    author_email='',
    description='Sphinx extension for deploying JupyterLite',
    license='BSD-3-Clause',
    zip_safe=True,
)
