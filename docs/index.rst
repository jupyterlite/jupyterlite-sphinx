jupyterlite-sphinx
==================

Installation
------------

You can install ``jupyterlite-sphinx`` with ``pip``:

.. code-block::

    pip install jupyterlite-sphinx

then you need to add the ``jupyterlite-sphinx`` extension to your ``conf.py`` file of your sphinx docs:

.. code-block:: python

    extensions = [
        'jupyterlite_sphinx',
        # And other sphinx extensions
        # ...
    ]

Replite directive
-----------------

``jupyterlite-sphinx`` provides a ``replite`` directive that allows you to embed a replite console in your docs.
This directive takes the same options as the ``replite`` package, see https://github.com/jtpio/replite for reference.

.. code-block:: rst

    .. replite::
       :kernel: python
       :toolbar: 1
       :theme: JupyterLab Light
       :width: 100%
       :height: 600px

        print('Hello, World!')

.. replite::
   :kernel: python
   :toolbar: 1
   :theme: JupyterLab Light
   :width: 100%
   :height: 600px

    print('Hello, World!')

Retrolite directive
-------------------

``jupyterlite-sphinx`` provides a ``retrolite`` directive that allows you to embed an entire executable Notebook in your docs.
It takes the name of the Notebook as argument:

.. code-block:: rst

    .. retrolite:: my_notebook.ipynb
       :width: 100%
       :height: 600px

.. retrolite:: my_notebook.ipynb
   :width: 100%
   :height: 600px

Or you can simply show the filetree:

.. code-block:: rst

    .. retrolite::
       :width: 100%
       :height: 600px

.. retrolite::
   :width: 100%
   :height: 600px


JupyterLab and RetroLab deployed for you
----------------------------------------

``jupyterlite-sphinx`` makes a full deployment of JupyterLite for you, you can access the JupyterLab UI and RetroLab UI following the
``./lite/lab/index.html`` and ``./lite/retro/index.html`` relative URLs:

`JupyterLab <./lite/lab/index.html>`_
`Retrolab <./lite/retro/index.html>`_

Configuration
-------------

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
