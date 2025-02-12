window.jupyterliteShowIframe = (tryItButtonId, iframeSrc) => {
  const tryItButton = document.getElementById(tryItButtonId);
  const iframe = document.createElement("iframe");
  const buttonRect = tryItButton.getBoundingClientRect();

  const spinner = document.createElement("div");
  // hardcoded spinner height and width needs to match what is in css.
  const spinnerHeight = 50; // px
  const spinnerWidth = 50; // px
  spinner.classList.add("jupyterlite_sphinx_spinner");
  spinner.style.display = "none";
  // Add negative margins to center the spinner
  spinner.style.marginTop = `-${spinnerHeight / 2}px`;
  spinner.style.marginLeft = `-${spinnerWidth / 2}px`;

  iframe.src = iframeSrc;
  iframe.width = iframe.height = "100%";
  iframe.classList.add("jupyterlite_sphinx_iframe");

  tryItButton.style.display = "none";
  spinner.style.display = "block";

  tryItButton.parentNode.appendChild(spinner);
  tryItButton.parentNode.appendChild(iframe);
};

window.jupyterliteConcatSearchParams = (iframeSrc, params) => {
  const baseURL = window.location.origin;
  const iframeUrl = new URL(iframeSrc, baseURL);

  let pageParams = new URLSearchParams(window.location.search);

  if (params === true) {
    params = Array.from(pageParams.keys());
  } else if (params === false) {
    params = [];
  } else if (!Array.isArray(params)) {
    console.error("The search parameters are not an array");
  }

  params.forEach((param) => {
    value = pageParams.get(param);
    if (value !== null) {
      iframeUrl.searchParams.append(param, value);
    }
  });

  if (iframeUrl.searchParams.size) {
    return `${iframeSrc.split("?")[0]}?${iframeUrl.searchParams.toString()}`;
  } else {
    return iframeSrc;
  }
};

window.tryExamplesShowIframe = (
  examplesContainerId,
  iframeContainerId,
  iframeParentContainerId,
  iframeSrc,
  iframeHeight,
) => {
  const examplesContainer = document.getElementById(examplesContainerId);
  const iframeParentContainer = document.getElementById(
    iframeParentContainerId,
  );
  const iframeContainer = document.getElementById(iframeContainerId);
  var height;

  let iframe = iframeContainer.querySelector(
    "iframe.jupyterlite_sphinx_iframe",
  );

  if (!iframe) {
    // Add spinner
    const spinner = document.createElement("div");
    // hardcoded spinner width needs to match what is in css.
    const spinnerHeight = 50; // px
    const spinnerWidth = 50; // px
    spinner.classList.add("jupyterlite_sphinx_spinner");
    iframeContainer.appendChild(spinner);

    const examples = examplesContainer.querySelector(".try_examples_content");
    iframe = document.createElement("iframe");
    iframe.src = iframeSrc;
    iframe.style.width = "100%";
    if (iframeHeight !== "None") {
      height = parseInt(iframeHeight);
    } else {
      height = Math.max(tryExamplesGlobalMinHeight, examples.offsetHeight);
    }

    /* Get spinner position. It will be centered in the iframe, unless the
     * iframe extends beyond the viewport, in which case it will be centered
     * between the top of the iframe and the bottom of the viewport.
     */
    const examplesTop = examples.getBoundingClientRect().top;
    const viewportBottom = window.innerHeight;
    const spinnerTop = 0.5 * Math.min(viewportBottom - examplesTop, height);
    spinner.style.top = `${spinnerTop}px`;
    // Add negative margins to center the spinner
    spinner.style.marginTop = `-${spinnerHeight / 2}px`;
    spinner.style.marginLeft = `-${spinnerWidth / 2}px`;

    iframe.style.height = `${height}px`;
    iframe.classList.add("jupyterlite_sphinx_iframe");
    examplesContainer.classList.add("hidden");

    iframeContainer.appendChild(iframe);
  } else {
    examplesContainer.classList.add("hidden");
  }
  iframeParentContainer.classList.remove("hidden");
};

window.tryExamplesHideIframe = (
  examplesContainerId,
  iframeParentContainerId,
) => {
  const examplesContainer = document.getElementById(examplesContainerId);
  const iframeParentContainer = document.getElementById(
    iframeParentContainerId,
  );

  iframeParentContainer.classList.add("hidden");
  examplesContainer.classList.remove("hidden");
};

// this will be used by the "Open in tab" button that is present next
// # to the "go back" button after an iframe is made visible.
window.openInNewTab = (examplesContainerId, iframeParentContainerId) => {
  const examplesContainer = document.getElementById(examplesContainerId);
  const iframeParentContainer = document.getElementById(
    iframeParentContainerId,
  );

  window.open(
    // we make some assumption that there is a single iframe and the the src is what we want to open.
    // Maybe we should have tabs open JupyterLab by default.
    iframeParentContainer.getElementsByTagName("iframe")[0].getAttribute("src"),
  );
  tryExamplesHideIframe(examplesContainerId, iframeParentContainerId);
};

/* Global variable for try_examples iframe minHeight. Defaults to 0 but can be
 * modified based on configuration in try_examples.json */
var tryExamplesGlobalMinHeight = 0;
/* Global variable to check if config has been loaded. This keeps it from getting
 * loaded multiple times if there are multiple try_examples directives on one page
 */
var tryExamplesConfigLoaded = false;

window.loadTryExamplesConfig = async (configFilePath) => {
  if (tryExamplesConfigLoaded) {
    return;
  }
  try {
    // Add a timestamp as query parameter to ensure a cached version of the
    // file is not used.
    const timestamp = new Date().getTime();
    const configFileUrl = `${configFilePath}?cb=${timestamp}`;
    const currentPageUrl = window.location.pathname;

    const response = await fetch(configFileUrl);
    if (!response.ok) {
      if (response.status === 404) {
        // Try examples ignore file is not present. Enable all interactive examples
        // in that case.
        console.log(
          "Optional try_examples config file not found. Enabling all interactive examples.",
        );

        // Grab all hidden try examples buttons and fade them in
        const buttons = document.getElementsByClassName(
          "try_examples_button hidden",
        );

        requestAnimationFrame(() => {
          for (let button of buttons) {
            button.style.opacity = "0";
            button.classList.remove("hidden");
            button.classList.add("fade-in");
            requestAnimationFrame(() => {
              button.style.opacity = "1";
            });
          }
        });

        tryExamplesConfigLoaded = true;

        return;
      }
      throw new Error(`Error fetching ${configFilePath}`);
    }

    const data = await response.json();
    if (!data) {
      // If config file exists but is empty, treat it like a missing config
      // and enable all interactive examples since there is no ignore pattern
      console.log(
        "Try examples config file is empty. Enabling all interactive examples.",
      );
      const buttons = document.getElementsByClassName(
        "try_examples_button hidden",
      );
      for (let button of buttons) {
        button.classList.remove("hidden");
      }
      return;
    }

    // Set minimum iframe height based on value in config file
    if (data.global_min_height) {
      tryExamplesGlobalMinHeight = parseInt(data.global_min_height);
    }

    // Selectively enable interactive examples if file matches one of the ignore patterns
    // by un-hiding try_examples_buttons with a smooth transition
    const Patterns = data.ignore_patterns || [];
    let shouldShowButtons = true;

    for (let pattern of Patterns) {
      let regex = new RegExp(pattern);
      if (regex.test(currentPageUrl)) {
        shouldShowButtons = false;
        break;
      }
    }

    if (shouldShowButtons) {
      const buttons = document.getElementsByClassName(
        "try_examples_button hidden",
      );
      requestAnimationFrame(() => {
        for (let button of buttons) {
          button.style.opacity = "0";
          button.classList.remove("hidden");
          button.classList.add("fade-in");
          requestAnimationFrame(() => {
            button.style.opacity = "1";
          });
        }
      });
    }
  } catch (error) {
    // On error, enable all buttons as a fallback to maintain current behavior
    console.error("Error loading try_examples config:", error);
    const buttons = document.getElementsByClassName(
      "try_examples_button hidden",
    );
    for (let button of buttons) {
      button.classList.remove("hidden");
    }
  }
  tryExamplesConfigLoaded = true;
};

window.toggleTryExamplesButtons = () => {
  /* Toggle visibility of TryExamples buttons. For use in console for debug
   * purposes. */
  var buttons = document.getElementsByClassName("try_examples_button hidden");

  for (var i = 0; i < buttons.length; i++) {
    buttons[i].classList.toggle("hidden");
  }
};
