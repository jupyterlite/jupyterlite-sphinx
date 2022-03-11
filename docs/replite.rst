Replite directive
=================

``jupyterlite-sphinx`` provides a ``replite`` directive that allows you to embed a replite console in your docs.
This directive takes the same options as the ``replite`` package, see https://github.com/jtpio/replite for reference.

.. code-block:: rst

    .. replite::
       :kernel: python
       :height: 600px

      import matplotlib.pyplot as plt
      import numpy as np

      x = np.linspace(0, 2 * np.pi, 200)
      y = np.sin(x)

      fig, ax = plt.subplots()
      ax.plot(x, y)
      plt.show()

.. replite::
   :kernel: python
   :height: 600px

    import matplotlib.pyplot as plt
    import numpy as np

    x = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()
