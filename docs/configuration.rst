Configuration
=============

JupyterLite-sphinx can be configured in your ``conf.py`` file by setting some global Python variables:

JupyterLite content
-------------------

You can embed custom content (notebooks and data files) in your JupyterLite build by providing the following config:

.. code-block:: python

    jupyterlite_contents = ["./path/to/my/notebooks/", "my_other_notebook.ipynb"]

JupyterLite dir
---------------

By default, jupyterlite-sphinx runs the ``jupyter lite build`` command in a temporary directory, you can overwrite this behavior and ask jupyterlite to build in a given directory:

.. code-block:: python

    # Build in the current directory
    jupyterlite_dir = "."

This allows for jupyterlite to automatically pick-up some paths https://jupyterlite.readthedocs.io/en/latest/reference/cli.html#the-lite-dir

JupyterLite config
------------------

You can provide `custom configuration <https://jupyterlite.readthedocs.io/en/latest/configuring.html>`_ to your JupyterLite deployment.

For example, if you want to have bqplot working in this deployment, you need to install the bqplot federated extension
and you can serve the bqplot wheel to ``piplite``, this is done by telling your ``conf.py`` where to look for the jupyterlite config:

.. code-block:: python

    jupyterlite_config = "jupyterlite_config.json"

The ``jupyterlite_config.json`` containing the following:

.. code-block:: json

    {
        "LiteBuildConfig": {
            "federated_extensions": [
                "https://conda.anaconda.org/conda-forge/noarch/bqplot-0.12.33-pyhd8ed1ab_0.tar.bz2",
            ],
            "ignore_sys_prefix": true,
            "piplite_urls": [
                "https://files.pythonhosted.org/packages/py2.py3/b/bqplot/bqplot-0.12.33-py2.py3-none-any.whl",
            ]
        }
    }

Then you should be able to show Notebooks working with bqplot!

.. code-block:: rst

    .. retrolite:: bqplot.ipynb

.. retrolite:: bqplot.ipynb
