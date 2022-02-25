jupyterlite-sphinx
==================

JupyterLab:
-----------

`JupyterLab <./lite/lab/index.html>`_

Retrolab:
---------

`Retrolab <./lite/retro/index.html>`_

.. toctree::
    :caption: Notebooks rendered with RetroLite:
    :maxdepth: 2

    NotebookLite

Replite directive:
------------------

`jupyterlite-sphinx` provides a `replite` directive that allows you to embed a replite console in your docs:

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
