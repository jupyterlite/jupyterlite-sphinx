# Replite directive

`jupyterlite-sphinx` provides a `replite` directive that allows you to embed a replite console in your docs.
This directive takes extra options which are the same options as the `replite` package, see <https://github.com/jtpio/replite> for reference.

```rst
.. replite::
   :kernel: xpython
   :height: 600px
   :prompt: Try Replite!
   :prompt_color: #dc3545

   import matplotlib.pyplot as plt
   import numpy as np

   x = np.linspace(0, 2 * np.pi, 200)
   y = np.sin(x)

   fig, ax = plt.subplots()
   ax.plot(x, y)
   plt.show()
```

```{eval-rst}
.. replite::
   :kernel: xpython
   :height: 600px
   :prompt: Try Replite!
   :prompt_color: #dc3545

   import matplotlib.pyplot as plt
   import numpy as np

   x = np.linspace(0, 2 * np.pi, 200)
   y = np.sin(x)

   fig, ax = plt.subplots()
   ax.plot(x, y)
   plt.show()
```

If the `:kernel:` parameter is not set to an installed kernel
(e.g. `xython` for xeus-python or `python` for Pyodide),
the REPL shows a selection dialog at startup.

If you use the `:new_tab:` option in the directive, the Replite console will be opened in a new browser tab
with the code pre-filled.

```rst
.. replite::
   :kernel: xpython
   :new_tab: True

   import matplotlib.pyplot as plt
   import numpy as np

   x = np.linspace(0, 2 * np.pi, 200)
   y = np.sin(x)

   fig, ax = plt.subplots()
   ax.plot(x, y)
   plt.show()
```

```{eval-rst}
.. replite::
   :kernel: xpython
   :new_tab: True

   import matplotlib.pyplot as plt
   import numpy as np

   x = np.linspace(0, 2 * np.pi, 200)
   y = np.sin(x)

   fig, ax = plt.subplots()
   ax.plot(x, y)
   plt.show()
```

When using this option, it is also possible to customise the button text, overriding the
global value using an additional `:new_tab_button_text:` parameter:

```rst
.. replite::
   :kernel: xpython
   :new_tab: True
   :new_tab_button_text: My custom Replite button text

   import matplotlib.pyplot as plt
   import numpy as np

   x = np.linspace(0, 2 * np.pi, 200)
   y = np.sin(x)

   fig, ax = plt.subplots()
   ax.plot(x, y)
   plt.show()
```

```{eval-rst}
.. replite::
   :kernel: xpython
   :new_tab: True
   :new_tab_button_text: My custom Replite button text

   import matplotlib.pyplot as plt
   import numpy as np

   x = np.linspace(0, 2 * np.pi, 200)
   y = np.sin(x)

   fig, ax = plt.subplots()
   ax.plot(x, y)
   plt.show()
```

````{tip}

   With `jupyterlite-core` **versions 0.5.0 and later**, it is also possible to disable the execution of
   the code in the Replite console by setting the `:execute:` option to `False`. This option defaults to `True`,
   and setting it has no effect in versions prior to 0.5.0.

   The behaviour can also be [configured globally](../configuration.md#replite-auto-execution-with-the-replite-directive)
   and then overridden in individual directives as needed.

```rst
.. replite::
   :kernel: xpython
   :new_tab: True # False works too
   :new_tab_button_text: Open REPL with the code execution disabled
   :execute: False

   import matplotlib.pyplot as plt
   import numpy as np

   x = np.linspace(0, 2 * np.pi, 200)
   y = np.sin(x)

   fig, ax = plt.subplots()
   ax.plot(x, y)
   plt.show()
```

```{eval-rst}
.. replite::
   :kernel: xpython
   :new_tab: True # False works too
   :new_tab_button_text: Open REPL with the code execution disabled
   :execute: False

   import matplotlib.pyplot as plt
   import numpy as np

   x = np.linspace(0, 2 * np.pi, 200)
   y = np.sin(x)

   fig, ax = plt.subplots()
   ax.plot(x, y)
   plt.show()
```

````
