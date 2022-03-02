Configuration
=============

You can provide custom configuration to your JupyterLite deployment.

For example, if you want to have bqplot working in this deployment, you need to install the bqplot federated extension
and you can serve the bqplot wheel to ``piplite``, this is done by telling your ``conf.py`` where to look for the jupyterlite config:

.. code-block:: python

    jupyterlite_config = "jupyterlite_config.json"

The ``jupyterlite_config.json`` containing the following:

.. code-block:: json

    {
        "LiteBuildConfig": {
            "federated_extensions": [
                "https://github.com/conda-forge/releases/releases/download/noarch/bqplot-0.12.33-pyhd8ed1ab_0.tar.bz2/bqplot-0.12.33-pyhd8ed1ab_0.tar.bz2",
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
