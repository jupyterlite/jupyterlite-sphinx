Replite directive
=================

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
