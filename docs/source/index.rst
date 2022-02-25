jupyterlite-sphinx
==================

JupyterLab:
-----------

`JupyterLab <./lite/lab/index.html>`_

Retrolab:
---------

`Retrolab <./lite/retro/index.html>`_

Replite directive:
------------------

`jupyterlite-sphinx` provides a `replite` directive that allows you to embed a replite console in your docs:

.. code-block:: rst

    .. replite::
       :kernel: python3

.. replite::
   :kernel: python3

.. code-block:: rst

    .. replite::
       :kernel: python3

        print('Hello, World!')

.. replite::
   :kernel: python3

    print('Hello, World!')

.. code-block:: rst

    .. replite::
       :kernel: python3
       :toolbar: 1
       :theme: JupyterLab Dark

        print('Hello, World!')

.. replite::
   :kernel: python3
   :toolbar: 1
   :theme: JupyterLab Dark

    print('Hello, World!')
