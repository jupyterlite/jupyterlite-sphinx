window.jupyterliteShowIframe = (tryItButtonId, iframeSrc) => {
  const tryItButton = document.getElementById(tryItButtonId);
  const iframe = document.createElement('iframe');

  iframe.src = iframeSrc;
  iframe.width = iframe.height = '100%';
  iframe.classList.add('jupyterlite_sphinx_iframe');

  tryItButton.parentNode.appendChild(iframe);
  tryItButton.innerText = 'Loading ...';
  tryItButton.classList.remove('jupyterlite_sphinx_try_it_button_unclicked');
  tryItButton.classList.add('jupyterlite_sphinx_try_it_button_clicked');
}

window.jupyterliteConcatSearchParams = (iframeSrc, params) => {
  const baseURL = window.location.origin;
  const iframeUrl = new URL(iframeSrc, baseURL);

  let pageParams = new URLSearchParams(window.location.search);

  if (params === true) {
    params = Array.from(pageParams.keys());
  } else if (params === false) {
    params = [];
  } else if (!Array.isArray(params)) {
    console.error('The search parameters are not an array');
  }

  params.forEach(param => {
    value = pageParams.get(param);
    if (value !== null) {
      iframeUrl.searchParams.append(param, value);
    }
  });

  return iframeUrl.toString().replace(baseURL, '');
}
