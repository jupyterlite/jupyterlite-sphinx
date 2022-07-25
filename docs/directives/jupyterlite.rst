JupyterLite directive
=====================

``jupyterlite-sphinx`` provides a ``jupyterlite`` directive that allows you to embed JupyterLab in your docs.

.. code-block:: rst

    .. jupyterlite::
       :width: 100%
       :height: 600px
       :prompt: Try JupyterLite!
       :prompt_color: #00aa42

.. jupyterlite::
   :width: 100%
   :height: 600px
   :prompt: Try JupyterLite!
   :prompt_color: #00aa42

You can also pass a Notebook file to open automatically:

.. code-block:: rst

    .. jupyterlite:: my_notebook.ipynb
       :width: 100%
       :height: 600px
       :prompt: Try JupyterLite!
       :prompt_color: #00aa42

.. jupyterlite:: my_notebook.ipynb
   :width: 100%
   :height: 600px
   :prompt: Try JupyterLite!
   :prompt_color: #00aa42
