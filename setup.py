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
        'sphinx>=4,<5',
        'jupyter_server',
        'jupyterlab_server',
    ],
    author='Martin Renou',
    author_email='martin.renou@gmail.com',
    description='Sphinx extension for deploying JupyterLite',
    license='MIT',
    zip_safe=True,
)
