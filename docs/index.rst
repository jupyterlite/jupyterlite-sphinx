jupyterlite-sphinx
==================

Installation:
-------------

You can install ``jupyterlite-sphinx`` with ``pip``:

.. code-block::

    pip install jupyterlite-sphinx

then you need to add the ``jupyterlite-sphinx`` extension to your ``conf.py`` file of your sphinx docs:

.. code-block:: python

    extensions = [
        'jupyterlite_sphinx',
        # And other extensions
        # ...
    ]

Replite directive:
------------------

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

Retrolite directive:
--------------------

``jupyterlite-sphinx`` provides a ``retrolite`` directive that allows you to embed an entire executable Notebook in your docs.
It takes the name of the Notebook as argument:

.. code-block:: rst

    .. retrolite:: my_notebook.ipynb

.. retrolite:: my_notebook.ipynb

JupyterLab and RetroLab deployed for you:
-----------------------------------------

``jupyterlite-sphinx`` makes a full deployment of JupyterLite for you, you can access the JupyterLab UI and RetroLab UI following the
``./lite/lab/index.html`` and ``./lite/retro/index.html`` relative URLs:

`JupyterLab <./lite/lab/index.html>`_
`Retrolab <./lite/retro/index.html>`_
