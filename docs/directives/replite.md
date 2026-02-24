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

````{tip}

   ## Additional REPL interface options (JupyterLite 0.6.0+)

   With `jupyterlite-core` versions 0.6.0 and later, the REPL interface comes with several additional customization options that provide more control over the execution environment and layout:

   ### Clearing cells on execute

   To automatically clear the previously executed cells when a new cell is executed, use the `:clear_cells_on_execute:` option:

   ```rst
   .. replite::
      :kernel: xeus-python
      :height: 600px
      :clear_cells_on_execute: True

      # When you execute this cell and then enter new code,
      # this cell will disappear from the display
      print("Hello, world!")
   ```

   ```{eval-rst}
   .. replite::
      :kernel: xeus-python
      :height: 600px
      :clear_cells_on_execute: True

      # When you execute this cell and then enter new code,
      # this cell will disappear from the display
      print("Hello, world!")
   ```

   ### Clearing code content on execute

   To automatically clear the code content in the prompt cell after execution, use the `:clear_code_on_execute:` option:

   ```rst
   .. replite::
      :kernel: xeus-python
      :height: 600px
      :clear_code_content_on_execute: True

      # After executing this cell, its content will be cleared,
      # but the output will remain visible
      print("The code will disappear but this output stays")
   ```

   ```{eval-rst}
   .. replite::
      :kernel: xeus-python
      :height: 600px
      :clear_code_content_on_execute: True

      # After executing this cell, its content will be cleared,
      # but the output will remain visible
      print("The code will disappear but this output stays")
   ```

   ### Hiding code input

   To hide the input cells after execution, showing only the output, use the `:hide_code_input:` option:

   ```rst
   .. replite::
      :kernel: xeus-python
      :height: 600px
      :hide_code_input: True

      # After executing this cell, the input will be hidden,
      # but the output will remain visible
      print("You'll see this output but not the code that generated it")
   ```

   ```{eval-rst}
   .. replite::
      :kernel: xeus-python
      :height: 600px
      :hide_code_input: True

      # After execution, this code will be hidden
      # Only the output will be visible
      print("You'll see this output but not the code that generated it")
   ```

   ### Changing prompt cell position

   By default, the prompt cell is positioned at the bottom of the REPL interface. You can change this using the `:prompt_cell_position:` option, which accepts `top`, `bottom`, `left`, or `right`:

   ```rst
   .. replite::
      :kernel: xeus-python
      :height: 600px
      :prompt_cell_position: top

      # The prompt will appear at the top of the REPL
      print("Input above, output below")
   ```

   ```{eval-rst}
   .. replite::
      :kernel: xeus-python
      :height: 600px
      :prompt_cell_position: top

      # The prompt will appear at the top of the REPL
      print("Input above, output below")
   ```

   ### Showing or hiding the kernel banner

   By default, the REPL shows the kernel banner with version information. To hide this banner, use the `:show_banner:` option:

   ```rst
   .. replite::
      :kernel: xeus-python
      :height: 600px
      :show_banner: False

      # The kernel banner won't be displayed
      print("No banner here")
   ```

   ```{eval-rst}
   .. replite::
      :kernel: xeus-python
      :height: 600px
      :show_banner: False

      # The kernel banner won't be displayed
      print("No banner here")
   ```

   ### Combining options

   All of these options can be combined to create a customised REPL experience,
   for example:

   ```rst
   .. replite::
      :kernel: xeus-python
      :prompt_cell_position: left
      :hide_code_input: True
      :show_banner: False
      :height: 400px

      # This will create a clean output-only display
      # with the input cell on the left
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
      :kernel: xeus-python
      :prompt_cell_position: left
      :hide_code_input: True
      :show_banner: False
      :height: 400px

      # This will create a clean output-only display
      # with the input cell on the left
      import matplotlib.pyplot as plt
      import numpy as np

      x = np.linspace(0, 2 * np.pi, 200)
      y = np.sin(x)

      fig, ax = plt.subplots()
      ax.plot(x, y)
      plt.show()
   ```

````

The parameters `:toolbar: 1`, `:showBanner: 0` and `:theme: …` can be used, respectively,
to enable toolbar buttons, not show the kernel's banner, and alter the REPL's appearance,
[as described in the JupyterLite REPL documentation](https://jupyterlite.readthedocs.io/en/latest/quickstart/embed-repl.html).
