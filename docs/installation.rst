Installation
============

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
