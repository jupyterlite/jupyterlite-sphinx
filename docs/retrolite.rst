RetroLite directive
===================

``jupyterlite-sphinx`` provides a ``retrolite`` directive that allows you to embed Retrolab in your docs.

.. code-block:: rst

    .. retrolite::
       :width: 100%
       :height: 600px

.. retrolite::
   :width: 100%
   :height: 600px

You can also pass a Notebook file to open:

.. code-block:: rst

    .. retrolite:: my_notebook.ipynb
       :width: 100%
       :height: 600px

.. retrolite:: my_notebook.ipynb
   :width: 100%
   :height: 600px
