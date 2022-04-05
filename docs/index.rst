jupyterlite-sphinx
==================

A Sphinx extension that provides utilities for embedding JupyterLite in your docs.

``jupyterlite-sphinx`` brings the power of JupyterLite to your Sphinx documentation. It makes a full JupyterLite deployment in your docs and provide some utilities for using that deployment easily.

.. replite::
   :kernel: python
   :toolbar: 0
   :theme: JupyterLab Light
   :width: 100%
   :height: 600px

   print("Hello from a JupyterLite console!")

.. toctree::
    :caption: Installation
    :maxdepth: 2

    installation
    configuration

.. toctree::
    :caption: Usage
    :maxdepth: 2

    directives/jupyterlite
    directives/retrolite
    directives/replite
    full
