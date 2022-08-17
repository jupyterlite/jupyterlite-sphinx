from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='jupyterlite-sphinx',
    version='0.7.2',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.7',
    install_requires=[
        'docutils',
        'jupyterlite[piplite]',
        'sphinx>=4,<5',
        'jupyter_server',
        'jupyterlab_server',
    ],
    author='JupyterLite Contributors',
    author_email='',
    description='Sphinx extension for deploying JupyterLite',
    license='BSD-3-Clause',
    zip_safe=True,
)
