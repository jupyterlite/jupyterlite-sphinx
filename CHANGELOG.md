# Changelog

<!-- <START NEW CHANGELOG ENTRY> -->

## 0.21.0

([Full Changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/v0.20.2...a9b1502e5071749c2bce66c0ac97ad1a54352cd1))

### Enhancements made

- Add `jupyterlite_ignore_contents` config, mapping to `--ignore-contents` arg in JupyterLite build [#309](https://github.com/jupyterlite/jupyterlite-sphinx/pull/309) ([@mfisher87](https://github.com/mfisher87))

### Maintenance and upkeep improvements

- Run `black` at pre-commit time [#311](https://github.com/jupyterlite/jupyterlite-sphinx/pull/311) ([@mfisher87](https://github.com/mfisher87))
- Gitignore `node_modules/` [#310](https://github.com/jupyterlite/jupyterlite-sphinx/pull/310) ([@mfisher87](https://github.com/mfisher87))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2025-06-03&to=2025-09-05&type=c))

[@mfisher87](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Amfisher87+updated%3A2025-06-03..2025-09-05&type=Issues) | [@pre-commit-ci](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Apre-commit-ci+updated%3A2025-06-03..2025-09-05&type=Issues)

<!-- <END NEW CHANGELOG ENTRY> -->

## 0.20.2

([Full Changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/v0.20.1...6cc40bf3ae417a5c827ce72750b5b6790ecd0c0d))

### Enhancements made

- Bump jupyterlite-core dependency [#299](https://github.com/jupyterlite/jupyterlite-sphinx/pull/299) ([@martinRenou](https://github.com/martinRenou))

### Maintenance and upkeep improvements

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2025-05-08&to=2025-06-03&type=c))

[@martinRenou](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3AmartinRenou+updated%3A2025-05-08..2025-06-03&type=Issues) | [@pre-commit-ci](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Apre-commit-ci+updated%3A2025-05-08..2025-06-03&type=Issues)

## 0.20.1

([Full Changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/v0.20.0...637c32e24fd5fe81459cab4e0c8f9d80d0789e15))

### Bugs fixed

- Fix `IndexError`s when the "Examples" is the last section in a docstring [#292](https://github.com/jupyterlite/jupyterlite-sphinx/pull/292) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))

### Maintenance and upkeep improvements

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2025-04-28&to=2025-05-08&type=c))

[@agriyakhetarpal](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Aagriyakhetarpal+updated%3A2025-04-28..2025-05-08&type=Issues) | [@jtpio](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Ajtpio+updated%3A2025-04-28..2025-05-08&type=Issues) | [@pre-commit-ci](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Apre-commit-ci+updated%3A2025-04-28..2025-05-08&type=Issues)

## 0.20.0

([Full Changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/v0.19.1...9a59d086cb22b57731d05365f7c10747ef9d2ad1))

### Enhancements made

- Allow adding contents from outside the Sphinx source directory [#280](https://github.com/jupyterlite/jupyterlite-sphinx/pull/280) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))
- Fix try button and shadows for dark theme [#279](https://github.com/jupyterlite/jupyterlite-sphinx/pull/279) ([@IsabelParedes](https://github.com/IsabelParedes))

### Bugs fixed

- Fix incorrect disable marker for `TryExamples` buttons [#284](https://github.com/jupyterlite/jupyterlite-sphinx/pull/284) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))

### Maintenance and upkeep improvements

- pin micromamba to v2.0.5 to fix failing RTD builds [#277](https://github.com/jupyterlite/jupyterlite-sphinx/pull/277) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2025-02-24&to=2025-04-28&type=c))

[@agriyakhetarpal](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Aagriyakhetarpal+updated%3A2025-02-24..2025-04-28&type=Issues) | [@IsabelParedes](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3AIsabelParedes+updated%3A2025-02-24..2025-04-28&type=Issues) | [@pre-commit-ci](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Apre-commit-ci+updated%3A2025-02-24..2025-04-28&type=Issues) | [@steppi](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Asteppi+updated%3A2025-02-24..2025-04-28&type=Issues)

## 0.19.1

([Full Changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/v0.19.0...1f2bb9736eef1b9c63e2f7659b8ff965ef02fe85))

### Bugs fixed

- BUG: Fix SciPy `make dist` doc workflow by ensuring jupyter is run with the current Python executable [#271](https://github.com/jupyterlite/jupyterlite-sphinx/pull/271) ([@steppi](https://github.com/steppi))

### Maintenance and upkeep improvements

### Documentation improvements

- Change button text contrast to comply with WCAG AA [#269](https://github.com/jupyterlite/jupyterlite-sphinx/pull/269) ([@mfisher87](https://github.com/mfisher87))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2025-02-12&to=2025-02-24&type=c))

[@mfisher87](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Amfisher87+updated%3A2025-02-12..2025-02-24&type=Issues) | [@pre-commit-ci](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Apre-commit-ci+updated%3A2025-02-12..2025-02-24&type=Issues) | [@steppi](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Asteppi+updated%3A2025-02-12..2025-02-24&type=Issues)

## 0.19.0

([Full Changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/v0.18.0...9cf9a249d02d99f68eb0c2ad49747607a19ba0b9))

### Enhancements made

- Better mobile device detection for interactive examples buttons [#250](https://github.com/jupyterlite/jupyterlite-sphinx/pull/250) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))

### Bugs fixed

- BUG: Fix list of possible docstring section header patterns for `global_enable_try_examples` [#263](https://github.com/jupyterlite/jupyterlite-sphinx/pull/263) ([@steppi](https://github.com/steppi))
- Add `ConfigLoader` with deduplicated logging and `try_examples` config caching [#249](https://github.com/jupyterlite/jupyterlite-sphinx/pull/249) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))

### Maintenance and upkeep improvements

- Update to `actions/upload-artifact@v4` [#267](https://github.com/jupyterlite/jupyterlite-sphinx/pull/267) ([@jtpio](https://github.com/jtpio))

### Documentation improvements

- Update documentation around fullscreen usage of `jupyterlite-sphinx` apps [#253](https://github.com/jupyterlite/jupyterlite-sphinx/pull/253) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2025-01-13&to=2025-02-12&type=c))

[@agriyakhetarpal](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Aagriyakhetarpal+updated%3A2025-01-13..2025-02-12&type=Issues) | [@jtpio](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Ajtpio+updated%3A2025-01-13..2025-02-12&type=Issues) | [@pre-commit-ci](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Apre-commit-ci+updated%3A2025-01-13..2025-02-12&type=Issues) | [@steppi](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Asteppi+updated%3A2025-01-13..2025-02-12&type=Issues)

## 0.18.0

([Full Changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/v0.17.1...a908c141dbbecfacdacf4a3382b526c30eda24d7))

### Enhancements made

- Allow enabling/disabling REPL code execution in the `Replite` directive [#245](https://github.com/jupyterlite/jupyterlite-sphinx/pull/245) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))

### Bugs fixed

- Correctly handle case where "See Also" section follows "Examples" in `global_enable_try_examples` [#251](https://github.com/jupyterlite/jupyterlite-sphinx/pull/251) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))

### Maintenance and upkeep improvements

- Drop Python 3.8 [#239](https://github.com/jupyterlite/jupyterlite-sphinx/pull/239) ([@jtpio](https://github.com/jtpio))
- Relax `jupyterlite-core` and `jupyterlite-xeus` dependencies [#238](https://github.com/jupyterlite/jupyterlite-sphinx/pull/238) ([@jtpio](https://github.com/jtpio))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2024-12-22&to=2025-01-13&type=c))

[@agriyakhetarpal](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Aagriyakhetarpal+updated%3A2024-12-22..2025-01-13&type=Issues) | [@jtpio](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Ajtpio+updated%3A2024-12-22..2025-01-13&type=Issues) | [@pre-commit-ci](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Apre-commit-ci+updated%3A2024-12-22..2025-01-13&type=Issues) | [@steppi](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Asteppi+updated%3A2024-12-22..2025-01-13&type=Issues)

## 0.17.1

([Full Changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/v0.17.0...f51bdc6e0971c45862af66eb68e10bfe6935f538))

### Bugs fixed

- Add missing dependency on `jupytext` [#236](https://github.com/jupyterlite/jupyterlite-sphinx/pull/236) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2024-12-22&to=2024-12-22&type=c))

[@agriyakhetarpal](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Aagriyakhetarpal+updated%3A2024-12-22..2024-12-22&type=Issues)

## 0.17.0

([Full Changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/v0.16.5...548b2151dfd593ae6633348e4df10348191495a9))

### Enhancements made

- Add a new-tabbed variant for the `Replite` directive, and allow customisation of its button text [#228](https://github.com/jupyterlite/jupyterlite-sphinx/pull/228) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))
- Allow global and custom button texts for the new-tabbed variants of the `JupyterLite`, `NotebookLite`, and the `Voici` directives [#227](https://github.com/jupyterlite/jupyterlite-sphinx/pull/227) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))
- Allow the use of a custom `overrides.json` file for configuring JupyterLite at runtime [#225](https://github.com/jupyterlite/jupyterlite-sphinx/pull/225) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))
- Add an option to open the Notebook UI and Voici apps in a new tab via the`NotebookLite` and `Voici` directives [#223](https://github.com/jupyterlite/jupyterlite-sphinx/pull/223) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))
- Support the usage of Markdown-based notebooks with "Lite" directives [#221](https://github.com/jupyterlite/jupyterlite-sphinx/pull/221) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))

### Bugs fixed

- Fix paths for Replite apps [#224](https://github.com/jupyterlite/jupyterlite-sphinx/pull/224) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))

### Maintenance and upkeep improvements

- Add some spacing below the Lite iframes [#235](https://github.com/jupyterlite/jupyterlite-sphinx/pull/235) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))
- Switch to Miniforge and drop Mambaforge [#233](https://github.com/jupyterlite/jupyterlite-sphinx/pull/233) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))
- Bump OS image and dependencies for Read the Docs build config [#229](https://github.com/jupyterlite/jupyterlite-sphinx/pull/229) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))
- Fix the opening of notebooks in a new tab when using the `JupyterLite`, `NotebookLite`, and `Voici` directives [#220](https://github.com/jupyterlite/jupyterlite-sphinx/pull/220) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2024-08-08&to=2024-12-22&type=c))

[@agriyakhetarpal](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Aagriyakhetarpal+updated%3A2024-08-08..2024-12-22&type=Issues) | [@pre-commit-ci](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Apre-commit-ci+updated%3A2024-08-08..2024-12-22&type=Issues) | [@steppi](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Asteppi+updated%3A2024-08-08..2024-12-22&type=Issues)

## 0.16.5

([Full Changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/v0.16.4...450a81d3a5e3a0ce0b56b67aafaa413323bc22b9))

### Bugs fixed

- Restore backwards compatibility with Sphinx \<8 [#201](https://github.com/jupyterlite/jupyterlite-sphinx/pull/201) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2024-08-07&to=2024-08-08&type=c))

[@agriyakhetarpal](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Aagriyakhetarpal+updated%3A2024-08-07..2024-08-08&type=Issues)

## 0.16.4

([Full Changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/v0.9.3...cf767125be27d1832c9a61ad3e46e7bb19c927ee))

### Enhancements made

- Strip tagged cells from `.ipynb` notebooks passed to the `NotebookLite` and `JupyterLite` directives [#180](https://github.com/jupyterlite/jupyterlite-sphinx/pull/180) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))
- Pass additional configuration options to the `jupyter lite build` command [#169](https://github.com/jupyterlite/jupyterlite-sphinx/pull/169) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))
- Add the option to open JupyterLite window in new tab [#165](https://github.com/jupyterlite/jupyterlite-sphinx/pull/165) ([@melissawm](https://github.com/melissawm))
- Allow usage of global configuration values for `TryExamples` directive if provided by user [#161](https://github.com/jupyterlite/jupyterlite-sphinx/pull/161) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))
- Minor refactor + typing info [#155](https://github.com/jupyterlite/jupyterlite-sphinx/pull/155) ([@Carreau](https://github.com/Carreau))
- Give a pragmatic solution to suppressing noisy output [#153](https://github.com/jupyterlite/jupyterlite-sphinx/pull/153) ([@steppi](https://github.com/steppi))
- Set lower default verbosity and add config options. [#150](https://github.com/jupyterlite/jupyterlite-sphinx/pull/150) ([@Carreau](https://github.com/Carreau))
- ENH: Add metadata for parallel_read_safe = True [#148](https://github.com/jupyterlite/jupyterlite-sphinx/pull/148) ([@steppi](https://github.com/steppi))
- Add option for initial warning cell in try examples directive [#143](https://github.com/jupyterlite/jupyterlite-sphinx/pull/143) ([@steppi](https://github.com/steppi))
- Hide buttons on smaller screens (mobile). [#141](https://github.com/jupyterlite/jupyterlite-sphinx/pull/141) ([@Carreau](https://github.com/Carreau))
- Suggestion: Add pre-commit to format js and css files. [#137](https://github.com/jupyterlite/jupyterlite-sphinx/pull/137) ([@Carreau](https://github.com/Carreau))
- Add a full screen "Open in tab" button [#135](https://github.com/jupyterlite/jupyterlite-sphinx/pull/135) ([@Carreau](https://github.com/Carreau))
- Add a loading spinner for TryExamples directive. [#133](https://github.com/jupyterlite/jupyterlite-sphinx/pull/133) ([@steppi](https://github.com/steppi))
- Misc parsing warnings. [#131](https://github.com/jupyterlite/jupyterlite-sphinx/pull/131) ([@Carreau](https://github.com/Carreau))
- Improve TryExamples customization [#129](https://github.com/jupyterlite/jupyterlite-sphinx/pull/129) ([@steppi](https://github.com/steppi))
- Add option to disable TryExamples without rebuilding docs [#118](https://github.com/jupyterlite/jupyterlite-sphinx/pull/118) ([@steppi](https://github.com/steppi))
- Add more configuration options to TryExamples directive and add documentation [#116](https://github.com/jupyterlite/jupyterlite-sphinx/pull/116) ([@steppi](https://github.com/steppi))
- Update to jupyterlite v0.2 [#113](https://github.com/jupyterlite/jupyterlite-sphinx/pull/113) ([@martinRenou](https://github.com/martinRenou))
- Add try_examples directive for adding interactivity to sphinx Examples sections [#111](https://github.com/jupyterlite/jupyterlite-sphinx/pull/111) ([@steppi](https://github.com/steppi))

### Bugs fixed

- Fix compatibility with Sphinx 8 [#199](https://github.com/jupyterlite/jupyterlite-sphinx/pull/199) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))
- Fix incorrect regex usage instructions for `TryExamples` JSON configuration file [#194](https://github.com/jupyterlite/jupyterlite-sphinx/pull/194) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))
- Restore SameFileError check when copying notebooks [#190](https://github.com/jupyterlite/jupyterlite-sphinx/pull/190) ([@melissawm](https://github.com/melissawm))
- Fix invalid schema for `jupyterlite_sphinx_strip` tag when `strip_tagged_cells` is `True` [#189](https://github.com/jupyterlite/jupyterlite-sphinx/pull/189) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))
- Resolve default-encoding errors on Windows [#187](https://github.com/jupyterlite/jupyterlite-sphinx/pull/187) ([@AA-Turner](https://github.com/AA-Turner))
- Hotfix: cell metadata to parse should be `jupyterlite_sphinx_strip` [#185](https://github.com/jupyterlite/jupyterlite-sphinx/pull/185) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))
- `TryExamples` directive: fix missing kernels in CircleCI deployments [#182](https://github.com/jupyterlite/jupyterlite-sphinx/pull/182) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))
- Issue 115 wrap fullscreen JupyterLite links [#181](https://github.com/jupyterlite/jupyterlite-sphinx/pull/181) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))
- Give a pragmatic solution to suppressing noisy output [#153](https://github.com/jupyterlite/jupyterlite-sphinx/pull/153) ([@steppi](https://github.com/steppi))
- Add processing of literal blocks in try examples directive [#134](https://github.com/jupyterlite/jupyterlite-sphinx/pull/134) ([@steppi](https://github.com/steppi))

### Maintenance and upkeep improvements

- Allow for JupyterLite 0.4.0 [#193](https://github.com/jupyterlite/jupyterlite-sphinx/pull/193) ([@jtpio](https://github.com/jtpio))
- Use the latest `jupyterlite-xeus` to fix the docs build [#179](https://github.com/jupyterlite/jupyterlite-sphinx/pull/179) ([@jtpio](https://github.com/jtpio))
- Update to `jupyterlite-core >=0.2,<0.4` [#160](https://github.com/jupyterlite/jupyterlite-sphinx/pull/160) ([@jtpio](https://github.com/jtpio))
- Update releaser workflows [#159](https://github.com/jupyterlite/jupyterlite-sphinx/pull/159) ([@jtpio](https://github.com/jtpio))
- Raise informative error message when building man on older sphinx [#158](https://github.com/jupyterlite/jupyterlite-sphinx/pull/158) ([@Carreau](https://github.com/Carreau))
- Add ruff pre-commit and reformat files with it [#156](https://github.com/jupyterlite/jupyterlite-sphinx/pull/156) ([@Carreau](https://github.com/Carreau))
- Minor refactor + typing info [#155](https://github.com/jupyterlite/jupyterlite-sphinx/pull/155) ([@Carreau](https://github.com/Carreau))
- Run pre-commit on all files in this repository. [#145](https://github.com/jupyterlite/jupyterlite-sphinx/pull/145) ([@Carreau](https://github.com/Carreau))
- Update publish workflow to use the PyPI trusted publisher [#123](https://github.com/jupyterlite/jupyterlite-sphinx/pull/123) ([@jtpio](https://github.com/jtpio))

### Documentation improvements

- Issue 115 wrap fullscreen JupyterLite links [#181](https://github.com/jupyterlite/jupyterlite-sphinx/pull/181) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))
- Some general formatting fixes (punctuation, backticks, etc.) [#172](https://github.com/jupyterlite/jupyterlite-sphinx/pull/172) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))
- Fix incorrect math processing [#139](https://github.com/jupyterlite/jupyterlite-sphinx/pull/139) ([@steppi](https://github.com/steppi))
- Update to `jupyterlite-xeus` [#138](https://github.com/jupyterlite/jupyterlite-sphinx/pull/138) ([@jtpio](https://github.com/jtpio))
- Improve TryExamples customization [#129](https://github.com/jupyterlite/jupyterlite-sphinx/pull/129) ([@steppi](https://github.com/steppi))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2023-09-13&to=2024-08-07&type=c))

[@AA-Turner](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3AAA-Turner+updated%3A2023-09-13..2024-08-07&type=Issues) | [@agriyakhetarpal](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Aagriyakhetarpal+updated%3A2023-09-13..2024-08-07&type=Issues) | [@Carreau](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3ACarreau+updated%3A2023-09-13..2024-08-07&type=Issues) | [@jtpio](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Ajtpio+updated%3A2023-09-13..2024-08-07&type=Issues) | [@martinRenou](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3AmartinRenou+updated%3A2023-09-13..2024-08-07&type=Issues) | [@matthewfeickert](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Amatthewfeickert+updated%3A2023-09-13..2024-08-07&type=Issues) | [@mattip](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Amattip+updated%3A2023-09-13..2024-08-07&type=Issues) | [@melissawm](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Amelissawm+updated%3A2023-09-13..2024-08-07&type=Issues) | [@pre-commit-ci](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Apre-commit-ci+updated%3A2023-09-13..2024-08-07&type=Issues) | [@steppi](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Asteppi+updated%3A2023-09-13..2024-08-07&type=Issues) | [@WarrenWeckesser](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3AWarrenWeckesser+updated%3A2023-09-13..2024-08-07&type=Issues)

## 0.16.3

([Full Changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/v0.16.2...d5d1cc1b9fb9f1446915dc98d36ed25ad2b2878f))

### Maintenance and upkeep improvements

- Allow for JupyterLite 0.4.0 [#193](https://github.com/jupyterlite/jupyterlite-sphinx/pull/193) ([@jtpio](https://github.com/jtpio))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2024-07-18&to=2024-07-31&type=c))

[@jtpio](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Ajtpio+updated%3A2024-07-18..2024-07-31&type=Issues) | [@pre-commit-ci](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Apre-commit-ci+updated%3A2024-07-18..2024-07-31&type=Issues)

## 0.16.2

([Full Changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/v0.16.1...45ba6d8bcd312ecbcb30f8e8db92d72dd8756faa))

### Bugs fixed

- Restore SameFileError check when copying notebooks [#190](https://github.com/jupyterlite/jupyterlite-sphinx/pull/190) ([@melissawm](https://github.com/melissawm))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2024-07-18&to=2024-07-18&type=c))

[@melissawm](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Amelissawm+updated%3A2024-07-18..2024-07-18&type=Issues)

## 0.16.1

([Full Changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/v0.16.0...a9c704ef2e1d602a87501bc3be284c842c0e8ff2))

### Bugs fixed

- Fix invalid schema for `jupyterlite_sphinx_strip` tag when `strip_tagged_cells` is `True` [#189](https://github.com/jupyterlite/jupyterlite-sphinx/pull/189) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2024-07-18&to=2024-07-18&type=c))

[@agriyakhetarpal](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Aagriyakhetarpal+updated%3A2024-07-18..2024-07-18&type=Issues)

## 0.16.0

([Full Changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/v0.15.0...4074ee2049947f1a537e8b822b5fb5643d4a42b3))

### Enhancements made

- Strip tagged cells from `.ipynb` notebooks passed to the `NotebookLite` and `JupyterLite` directives [#180](https://github.com/jupyterlite/jupyterlite-sphinx/pull/180) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))

### Bugs fixed

- Resolve default-encoding errors on Windows [#187](https://github.com/jupyterlite/jupyterlite-sphinx/pull/187) ([@AA-Turner](https://github.com/AA-Turner))
- Hotfix: cell metadata to parse should be `jupyterlite_sphinx_strip` [#185](https://github.com/jupyterlite/jupyterlite-sphinx/pull/185) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))
- `TryExamples` directive: fix missing kernels in CircleCI deployments [#182](https://github.com/jupyterlite/jupyterlite-sphinx/pull/182) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))
- Issue 115 wrap fullscreen JupyterLite links [#181](https://github.com/jupyterlite/jupyterlite-sphinx/pull/181) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))

### Maintenance and upkeep improvements

- Use the latest `jupyterlite-xeus` to fix the docs build [#179](https://github.com/jupyterlite/jupyterlite-sphinx/pull/179) ([@jtpio](https://github.com/jtpio))

### Documentation improvements

- Issue 115 wrap fullscreen JupyterLite links [#181](https://github.com/jupyterlite/jupyterlite-sphinx/pull/181) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2024-05-16&to=2024-07-18&type=c))

[@AA-Turner](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3AAA-Turner+updated%3A2024-05-16..2024-07-18&type=Issues) | [@agriyakhetarpal](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Aagriyakhetarpal+updated%3A2024-05-16..2024-07-18&type=Issues) | [@Carreau](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3ACarreau+updated%3A2024-05-16..2024-07-18&type=Issues) | [@jtpio](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Ajtpio+updated%3A2024-05-16..2024-07-18&type=Issues) | [@pre-commit-ci](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Apre-commit-ci+updated%3A2024-05-16..2024-07-18&type=Issues) | [@steppi](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Asteppi+updated%3A2024-05-16..2024-07-18&type=Issues)

## 0.15.0

([Full Changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/v0.14.0...90a0b6327c1b2b3badaf925aa08e9a54083b4492))

### Enhancements made

- Pass additional configuration options to the `jupyter lite build` command [#169](https://github.com/jupyterlite/jupyterlite-sphinx/pull/169) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))
- Add the option to open JupyterLite window in new tab [#165](https://github.com/jupyterlite/jupyterlite-sphinx/pull/165) ([@melissawm](https://github.com/melissawm))

### Maintenance and upkeep improvements

### Documentation improvements

- Some general formatting fixes (punctuation, backticks, etc.) [#172](https://github.com/jupyterlite/jupyterlite-sphinx/pull/172) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2024-04-30&to=2024-05-16&type=c))

[@agriyakhetarpal](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Aagriyakhetarpal+updated%3A2024-04-30..2024-05-16&type=Issues) | [@melissawm](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Amelissawm+updated%3A2024-04-30..2024-05-16&type=Issues) | [@pre-commit-ci](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Apre-commit-ci+updated%3A2024-04-30..2024-05-16&type=Issues) | [@steppi](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Asteppi+updated%3A2024-04-30..2024-05-16&type=Issues)

## 0.14.0

([Full Changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/v0.13.1...cefbabe2d87e3572f6627c9a6f27923a6f8b8b82))

### Enhancements made

- Allow usage of global configuration values for `TryExamples` directive if provided by user [#161](https://github.com/jupyterlite/jupyterlite-sphinx/pull/161) ([@agriyakhetarpal](https://github.com/agriyakhetarpal))
- Minor refactor + typing info [#155](https://github.com/jupyterlite/jupyterlite-sphinx/pull/155) ([@Carreau](https://github.com/Carreau))

### Maintenance and upkeep improvements

- Update to `jupyterlite-core >=0.2,<0.4` [#160](https://github.com/jupyterlite/jupyterlite-sphinx/pull/160) ([@jtpio](https://github.com/jtpio))
- Update releaser workflows [#159](https://github.com/jupyterlite/jupyterlite-sphinx/pull/159) ([@jtpio](https://github.com/jtpio))
- Raise informative error message when building man on older sphinx [#158](https://github.com/jupyterlite/jupyterlite-sphinx/pull/158) ([@Carreau](https://github.com/Carreau))
- Add ruff pre-commit and reformat files with it [#156](https://github.com/jupyterlite/jupyterlite-sphinx/pull/156) ([@Carreau](https://github.com/Carreau))
- Minor refactor + typing info [#155](https://github.com/jupyterlite/jupyterlite-sphinx/pull/155) ([@Carreau](https://github.com/Carreau))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2024-03-22&to=2024-04-30&type=c))

[@agriyakhetarpal](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Aagriyakhetarpal+updated%3A2024-03-22..2024-04-30&type=Issues) | [@Carreau](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3ACarreau+updated%3A2024-03-22..2024-04-30&type=Issues) | [@jtpio](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Ajtpio+updated%3A2024-03-22..2024-04-30&type=Issues) | [@pre-commit-ci](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Apre-commit-ci+updated%3A2024-03-22..2024-04-30&type=Issues) | [@steppi](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Asteppi+updated%3A2024-03-22..2024-04-30&type=Issues)

## 0.13.1

([Full Changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/v0.13.0...1e80dd142b70c883f7fcc5de4823fe7ca81bfb32))

### Enhancements made

- Give a pragmatic solution to suppressing noisy output [#153](https://github.com/jupyterlite/jupyterlite-sphinx/pull/153) ([@steppi](https://github.com/steppi))

### Bugs fixed

- Give a pragmatic solution to suppressing noisy output [#153](https://github.com/jupyterlite/jupyterlite-sphinx/pull/153) ([@steppi](https://github.com/steppi))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2024-03-19&to=2024-03-22&type=c))

[@steppi](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Asteppi+updated%3A2024-03-19..2024-03-22&type=Issues)

## 0.13.0

([Full Changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/v0.12.0...4dd4b3074d1a8e573c76b331a7ed20ff886bde2e))

### Enhancements made

- Set lower default verbosity and add config options. [#150](https://github.com/jupyterlite/jupyterlite-sphinx/pull/150) ([@Carreau](https://github.com/Carreau))
- ENH: Add metadata for parallel_read_safe = True [#148](https://github.com/jupyterlite/jupyterlite-sphinx/pull/148) ([@steppi](https://github.com/steppi))

### Maintenance and upkeep improvements

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2024-03-07&to=2024-03-19&type=c))

[@Carreau](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3ACarreau+updated%3A2024-03-07..2024-03-19&type=Issues) | [@pre-commit-ci](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Apre-commit-ci+updated%3A2024-03-07..2024-03-19&type=Issues) | [@steppi](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Asteppi+updated%3A2024-03-07..2024-03-19&type=Issues)

## 0.12.0

([Full Changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/v0.11.0...0ef8be22f403e6ebaa46d1b6e1643ce7303a756c))

### Enhancements made

- Add option for initial warning cell in try examples directive [#143](https://github.com/jupyterlite/jupyterlite-sphinx/pull/143) ([@steppi](https://github.com/steppi))
- Hide buttons on smaller screens (mobile). [#141](https://github.com/jupyterlite/jupyterlite-sphinx/pull/141) ([@Carreau](https://github.com/Carreau))
- Suggestion: Add pre-commit to format js and css files. [#137](https://github.com/jupyterlite/jupyterlite-sphinx/pull/137) ([@Carreau](https://github.com/Carreau))
- Add a full screen "Open in tab" button [#135](https://github.com/jupyterlite/jupyterlite-sphinx/pull/135) ([@Carreau](https://github.com/Carreau))
- Add a loading spinner for TryExamples directive. [#133](https://github.com/jupyterlite/jupyterlite-sphinx/pull/133) ([@steppi](https://github.com/steppi))
- Misc parsing warnings. [#131](https://github.com/jupyterlite/jupyterlite-sphinx/pull/131) ([@Carreau](https://github.com/Carreau))
- Improve TryExamples customization [#129](https://github.com/jupyterlite/jupyterlite-sphinx/pull/129) ([@steppi](https://github.com/steppi))
- Add option to disable TryExamples without rebuilding docs [#118](https://github.com/jupyterlite/jupyterlite-sphinx/pull/118) ([@steppi](https://github.com/steppi))

### Bugs fixed

- Add processing of literal blocks in try examples directive [#134](https://github.com/jupyterlite/jupyterlite-sphinx/pull/134) ([@steppi](https://github.com/steppi))

### Maintenance and upkeep improvements

- Run pre-commit on all files in this repository. [#145](https://github.com/jupyterlite/jupyterlite-sphinx/pull/145) ([@Carreau](https://github.com/Carreau))
- Update publish workflow to use the PyPI trusted publisher [#123](https://github.com/jupyterlite/jupyterlite-sphinx/pull/123) ([@jtpio](https://github.com/jtpio))

### Documentation improvements

- Fix incorrect math processing [#139](https://github.com/jupyterlite/jupyterlite-sphinx/pull/139) ([@steppi](https://github.com/steppi))
- Update to `jupyterlite-xeus` [#138](https://github.com/jupyterlite/jupyterlite-sphinx/pull/138) ([@jtpio](https://github.com/jtpio))
- Improve TryExamples customization [#129](https://github.com/jupyterlite/jupyterlite-sphinx/pull/129) ([@steppi](https://github.com/steppi))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2023-12-22&to=2024-03-07&type=c))

[@Carreau](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3ACarreau+updated%3A2023-12-22..2024-03-07&type=Issues) | [@jtpio](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Ajtpio+updated%3A2023-12-22..2024-03-07&type=Issues) | [@martinRenou](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3AmartinRenou+updated%3A2023-12-22..2024-03-07&type=Issues) | [@mattip](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Amattip+updated%3A2023-12-22..2024-03-07&type=Issues) | [@steppi](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Asteppi+updated%3A2023-12-22..2024-03-07&type=Issues)

## 0.11.0

([Full Changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/v0.10.0...b1535878aef8233dfea9136fa8fa43c76a9b81e8))

### Enhancements made

- Add more configuration options to TryExamples directive and add documentation [#116](https://github.com/jupyterlite/jupyterlite-sphinx/pull/116) ([@steppi](https://github.com/steppi))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2023-11-09&to=2023-12-22&type=c))

[@steppi](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Asteppi+updated%3A2023-11-09..2023-12-22&type=Issues)

## 0.10.0

([Full Changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/v0.9.3...72393f736e38f36ff6f91a3ae878ba3f54646cad))

### Enhancements made

- Update to jupyterlite v0.2 [#113](https://github.com/jupyterlite/jupyterlite-sphinx/pull/113) ([@martinRenou](https://github.com/martinRenou))
- Add try_examples directive for adding interactivity to sphinx Examples sections [#111](https://github.com/jupyterlite/jupyterlite-sphinx/pull/111) ([@steppi](https://github.com/steppi))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2023-09-13&to=2023-11-09&type=c))

[@martinRenou](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3AmartinRenou+updated%3A2023-09-13..2023-11-09&type=Issues) | [@steppi](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Asteppi+updated%3A2023-09-13..2023-11-09&type=Issues)

## 0.9.3

([Full Changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/v0.9.2...551a58744536dca3d51e657b1d7ddcb5da102510))

### Bugs fixed

- Fix search params [#109](https://github.com/jupyterlite/jupyterlite-sphinx/pull/109) ([@brichet](https://github.com/brichet))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2023-09-11&to=2023-09-13&type=c))

[@brichet](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Abrichet+updated%3A2023-09-11..2023-09-13&type=Issues)

## 0.9.2

([Full Changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/v0.9.1...d69ce1f546d58cb81cb7a976358712a440f842d1))

### Enhancements made

- Transfer search parameters from page URL to jupyterlite [#108](https://github.com/jupyterlite/jupyterlite-sphinx/pull/108) ([@brichet](https://github.com/brichet))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2023-07-24&to=2023-09-11&type=c))

[@brichet](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Abrichet+updated%3A2023-07-24..2023-09-11&type=Issues) | [@martinRenou](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3AmartinRenou+updated%3A2023-07-24..2023-09-11&type=Issues)

## 0.9.1

([Full Changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/v0.9.0...97014e26a62170f0d468918b3dc6c4ceeca28c26))

### Bugs fixed

- Remove Apps config auto-computation [#104](https://github.com/jupyterlite/jupyterlite-sphinx/pull/104) ([@martinRenou](https://github.com/martinRenou))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2023-06-30&to=2023-07-24&type=c))

[@martinRenou](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3AmartinRenou+updated%3A2023-06-30..2023-07-24&type=Issues)

## 0.9.0

([Full Changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/v0.8.0...e22a7e66b17cb87c499487f28761f4fa32f8b061))

### Enhancements made

- Add Voici directive [#100](https://github.com/jupyterlite/jupyterlite-sphinx/pull/100) ([@martinRenou](https://github.com/martinRenou))
- Default lite directory to the docs directory [#99](https://github.com/jupyterlite/jupyterlite-sphinx/pull/99) ([@martinRenou](https://github.com/martinRenou))
- Use xeus-python in docs [#98](https://github.com/jupyterlite/jupyterlite-sphinx/pull/98) ([@martinRenou](https://github.com/martinRenou))

### Maintenance and upkeep improvements

- Update to `jupyterlite-core==0.1.0`, require Python 3.8 [#96](https://github.com/jupyterlite/jupyterlite-sphinx/pull/96) ([@jtpio](https://github.com/jtpio))

### Documentation improvements

- Add conda instructions and docs scripts [#97](https://github.com/jupyterlite/jupyterlite-sphinx/pull/97) ([@jtpio](https://github.com/jtpio))
- Update docs to mention adding other kernels [#94](https://github.com/jupyterlite/jupyterlite-sphinx/pull/94) ([@jtpio](https://github.com/jtpio))
- Add changelog to the docs, more markdown [#93](https://github.com/jupyterlite/jupyterlite-sphinx/pull/93) ([@jtpio](https://github.com/jtpio))
- Convert docs to Markdown [#92](https://github.com/jupyterlite/jupyterlite-sphinx/pull/92) ([@jtpio](https://github.com/jtpio))
- Add notice about `jupyterlite-core` in the changelog [#91](https://github.com/jupyterlite/jupyterlite-sphinx/pull/91) ([@jtpio](https://github.com/jtpio))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2023-03-15&to=2023-06-30&type=c))

[@jtpio](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Ajtpio+updated%3A2023-03-15..2023-06-30&type=Issues) | [@martinRenou](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3AmartinRenou+updated%3A2023-03-15..2023-06-30&type=Issues)

## 0.8.0

([Full Changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/0.7.3...51e489426a2e0026bcbc7207c87764bcd936d78b))

⚠️ `jupyterlite-sphinx` now depends on `jupyterlite-core` ⚠️

`jupyterlite-sphinx` now depends on the `jupyterlite-core` package instead of `jupyterlite`.

The `jupyterlite-core` package provides the core functionality for building JupyterLite websites, the CLI and [extension points](https://jupyterlite.readthedocs.io/en/latest/howto/extensions/cli-addons.html). Currently it only includes a JavaScript kernel that runs in Web Worker. If you would like to include a Python kernel in your deployment you will have to add it to your dependencies, for example with:

```
python -m pip install jupyterlite-pyodide-kernel
```

Or next to the `jupyterlite-sphinx` dependency:

```
jupyterlite-sphinx
jupyterlite-pyodide-kernel
```

### Maintenance and upkeep improvements

- Depend on `jupyterlite-core` [#89](https://github.com/jupyterlite/jupyterlite-sphinx/pull/89) ([@jtpio](https://github.com/jtpio))
- Add releaser workflows and changelog [#86](https://github.com/jupyterlite/jupyterlite-sphinx/pull/86) ([@jtpio](https://github.com/jtpio))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2023-02-03&to=2023-03-15&type=c))

[@jtpio](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Ajtpio+updated%3A2023-02-03..2023-03-15&type=Issues)

## 0.7.3

([full changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/b8a4dec...6ccb288))

### Documentation improvements

- Update the `piplite_urls` configuration [#79](https://github.com/jupyterlite/jupyterlite-sphinx/pull/79) ([@jtpio](https://github.com/jtpio))

### Other merged PRs

- Unpin sphinx [#85](https://github.com/jupyterlite/jupyterlite-sphinx/pull/85) ([@lesteve](https://github.com/lesteve))
- add a github link to the documentation [#82](https://github.com/jupyterlite/jupyterlite-sphinx/pull/82) ([@12rambau](https://github.com/12rambau))
- DOC fix broken link to custom Jupyterlite configuration [#78](https://github.com/jupyterlite/jupyterlite-sphinx/pull/78) ([@lesteve](https://github.com/lesteve))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2022-08-17&to=2023-02-03&type=c))

[@12rambau](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3A12rambau+updated%3A2022-08-17..2023-02-03&type=Issues) | [@jtpio](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Ajtpio+updated%3A2022-08-17..2023-02-03&type=Issues) | [@lesteve](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Alesteve+updated%3A2022-08-17..2023-02-03&type=Issues) | [@martinRenou](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3AmartinRenou+updated%3A2022-08-17..2023-02-03&type=Issues)

## 0.7.2

([full changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/3927797...b8a4dec))

### Merged PRs

- Finish reverting config names. [#74](https://github.com/jupyterlite/jupyterlite-sphinx/pull/74) ([@jasongrout](https://github.com/jasongrout))
- Restore jupyterlite_contents being optionally a string [#73](https://github.com/jupyterlite/jupyterlite-sphinx/pull/73) ([@jasongrout-db](https://github.com/jasongrout-db))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2022-08-16&to=2022-08-17&type=c))

[@jasongrout](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Ajasongrout+updated%3A2022-08-16..2022-08-17&type=Issues) | [@jasongrout-db](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Ajasongrout-db+updated%3A2022-08-16..2022-08-17&type=Issues)

## 0.7.1

([full changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/65d951e...3927797))

### Merged PRs

- Make the jupyterlite_contents glob recursive. [#72](https://github.com/jupyterlite/jupyterlite-sphinx/pull/72) ([@jasongrout](https://github.com/jasongrout))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2022-07-26&to=2022-08-16&type=c))

[@jasongrout](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Ajasongrout+updated%3A2022-07-26..2022-08-16&type=Issues)

## 0.7.0

([full changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/88c3dfd...65d951e))

### Merged PRs

- "Try It Live!" button [#67](https://github.com/jupyterlite/jupyterlite-sphinx/pull/67) ([@martinRenou](https://github.com/martinRenou))
- Make .ipynb source binding an opt-out [#66](https://github.com/jupyterlite/jupyterlite-sphinx/pull/66) ([@martinRenou](https://github.com/martinRenou))
- add globbing to content [#64](https://github.com/jupyterlite/jupyterlite-sphinx/pull/64) ([@amueller](https://github.com/amueller))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2022-06-28&to=2022-07-26&type=c))

[@12rambau](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3A12rambau+updated%3A2022-06-28..2022-07-26&type=Issues) | [@amueller](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Aamueller+updated%3A2022-06-28..2022-07-26&type=Issues) | [@jtpio](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Ajtpio+updated%3A2022-06-28..2022-07-26&type=Issues) | [@martinRenou](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3AmartinRenou+updated%3A2022-06-28..2022-07-26&type=Issues)

## 0.6.0

([full changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/c323ed1...88c3dfd))

### Maintenance and upkeep improvements

- Remove unneeded code [#60](https://github.com/jupyterlite/jupyterlite-sphinx/pull/60) ([@jtpio](https://github.com/jtpio))

### Other merged PRs

- Revert renaming the config properties [#62](https://github.com/jupyterlite/jupyterlite-sphinx/pull/62) ([@martinRenou](https://github.com/martinRenou))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2022-06-24&to=2022-06-28&type=c))

[@jtpio](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Ajtpio+updated%3A2022-06-24..2022-06-28&type=Issues) | [@martinRenou](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3AmartinRenou+updated%3A2022-06-24..2022-06-28&type=Issues)

## 0.5.0

([full changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/0223c17...c323ed1))

### Enhancements made

- More consistent naming [#58](https://github.com/jupyterlite/jupyterlite-sphinx/pull/58) ([@martinRenou](https://github.com/martinRenou))

### Other merged PRs

- Update Pypi description to be the same as the readme [#59](https://github.com/jupyterlite/jupyterlite-sphinx/pull/59) ([@jasongrout](https://github.com/jasongrout))
- Add jupyterlite_contents config [#24](https://github.com/jupyterlite/jupyterlite-sphinx/pull/24) ([@martinRenou](https://github.com/martinRenou))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2022-06-21&to=2022-06-24&type=c))

[@jasongrout](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Ajasongrout+updated%3A2022-06-21..2022-06-24&type=Issues) | [@martinRenou](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3AmartinRenou+updated%3A2022-06-21..2022-06-24&type=Issues)

## 0.4.9

([full changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/ebc5770...0223c17))

### Merged PRs

- Add jupyterlite_dir config option [#16](https://github.com/jupyterlite/jupyterlite-sphinx/pull/16) ([@martinRenou](https://github.com/martinRenou))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2022-06-17&to=2022-06-21&type=c))

[@martinRenou](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3AmartinRenou+updated%3A2022-06-17..2022-06-21&type=Issues)

## 0.4.8

([full changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/7ee0c09...ebc5770))

### Enhancements made

- Run jupyter lite with subprocess.run to not suppress stdout [#55](https://github.com/jupyterlite/jupyterlite-sphinx/pull/55) ([@jasongrout](https://github.com/jasongrout))
- Adopt the path convention of other directives like literalinclude [#54](https://github.com/jupyterlite/jupyterlite-sphinx/pull/54) ([@jasongrout](https://github.com/jasongrout))

### Bugs fixed

- Fix federated extensions URLs [#56](https://github.com/jupyterlite/jupyterlite-sphinx/pull/56) ([@martinRenou](https://github.com/martinRenou))
- Allow whitespace in filenames [#52](https://github.com/jupyterlite/jupyterlite-sphinx/pull/52) ([@jasongrout](https://github.com/jasongrout))

### Other merged PRs

- Clarify how to preview locally, view a notebook in fullscreen, and link config docs [#45](https://github.com/jupyterlite/jupyterlite-sphinx/pull/45) ([@joelostblom](https://github.com/joelostblom))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2022-04-05&to=2022-06-17&type=c))

[@jasongrout](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Ajasongrout+updated%3A2022-04-05..2022-06-17&type=Issues) | [@joelostblom](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Ajoelostblom+updated%3A2022-04-05..2022-06-17&type=Issues) | [@martinRenou](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3AmartinRenou+updated%3A2022-04-05..2022-06-17&type=Issues)

## 0.4.7

([full changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/78aa5b3...7ee0c09))

### Merged PRs

- Improve iframe URL [#43](https://github.com/jupyterlite/jupyterlite-sphinx/pull/43) ([@martinRenou](https://github.com/martinRenou))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2022-03-29&to=2022-04-05&type=c))

[@martinRenou](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3AmartinRenou+updated%3A2022-03-29..2022-04-05&type=Issues)

## 0.4.6

([full changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/9d98a8e...78aa5b3))

### Merged PRs

- Replite code: Remove empty lines but not indentation  [#42](https://github.com/jupyterlite/jupyterlite-sphinx/pull/42) ([@martinRenou](https://github.com/martinRenou))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2022-03-28&to=2022-03-29&type=c))

[@martinRenou](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3AmartinRenou+updated%3A2022-03-28..2022-03-29&type=Issues)

## 0.4.5

([full changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/b0e17a9...9d98a8e))

### Merged PRs

- Cleanup query strings with urllib [#41](https://github.com/jupyterlite/jupyterlite-sphinx/pull/41) ([@martinRenou](https://github.com/martinRenou))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2022-03-15&to=2022-03-28&type=c))

[@martinRenou](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3AmartinRenou+updated%3A2022-03-15..2022-03-28&type=Issues)

## 0.4.4

([full changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/506d16e...b0e17a9))

### Merged PRs

- Revert link fix [#35](https://github.com/jupyterlite/jupyterlite-sphinx/pull/35) ([@martinRenou](https://github.com/martinRenou))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2022-03-14&to=2022-03-15&type=c))

[@martinRenou](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3AmartinRenou+updated%3A2022-03-14..2022-03-15&type=Issues)

## 0.4.3

([full changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/e9fc847...506d16e))

### Merged PRs

- Fix lite links [#32](https://github.com/jupyterlite/jupyterlite-sphinx/pull/32) ([@martinRenou](https://github.com/martinRenou))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2022-03-14&to=2022-03-14&type=c))

[@martinRenou](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3AmartinRenou+updated%3A2022-03-14..2022-03-14&type=Issues)

## 0.4.2

([full changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/60aeb58...e9fc847))

### Merged PRs

- Replite: Fix multiline support [#30](https://github.com/jupyterlite/jupyterlite-sphinx/pull/30) ([@martinRenou](https://github.com/martinRenou))
- Bail early if there was an error [#29](https://github.com/jupyterlite/jupyterlite-sphinx/pull/29) ([@martinRenou](https://github.com/martinRenou))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2022-03-09&to=2022-03-14&type=c))

[@martinRenou](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3AmartinRenou+updated%3A2022-03-09..2022-03-14&type=Issues)

## 0.4.1

([full changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/21e2dbe...60aeb58))

### Merged PRs

- Make sure we don't add the ipynb source prefix twice [#28](https://github.com/jupyterlite/jupyterlite-sphinx/pull/28) ([@martinRenou](https://github.com/martinRenou))
- Add LICENSE and update author [#26](https://github.com/jupyterlite/jupyterlite-sphinx/pull/26) ([@martinRenou](https://github.com/martinRenou))
- Fix sphinx pinning [#25](https://github.com/jupyterlite/jupyterlite-sphinx/pull/25) ([@martinRenou](https://github.com/martinRenou))
- Add Jupyterlite logo to the docs [#22](https://github.com/jupyterlite/jupyterlite-sphinx/pull/22) ([@martinRenou](https://github.com/martinRenou))
- Improve documentation frontpage [#20](https://github.com/jupyterlite/jupyterlite-sphinx/pull/20) ([@martinRenou](https://github.com/martinRenou))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2022-03-02&to=2022-03-09&type=c))

[@martinRenou](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3AmartinRenou+updated%3A2022-03-02..2022-03-09&type=Issues)

## 0.4.0

([full changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/d781ca9...21e2dbe))

### Merged PRs

- Add jupyterlite directive and rework docs [#19](https://github.com/jupyterlite/jupyterlite-sphinx/pull/19) ([@martinRenou](https://github.com/martinRenou))
- Retrolite directive: Show tree if no Notebook specified [#18](https://github.com/jupyterlite/jupyterlite-sphinx/pull/18) ([@martinRenou](https://github.com/martinRenou))
- Remove docs build from the CI [#15](https://github.com/jupyterlite/jupyterlite-sphinx/pull/15) ([@martinRenou](https://github.com/martinRenou))
- Fix notebook search [#14](https://github.com/jupyterlite/jupyterlite-sphinx/pull/14) ([@martinRenou](https://github.com/martinRenou))
- Updating docs [#10](https://github.com/jupyterlite/jupyterlite-sphinx/pull/10) ([@martinRenou](https://github.com/martinRenou))
- Add link to the ipycanvas docs in the README [#9](https://github.com/jupyterlite/jupyterlite-sphinx/pull/9) ([@martinRenou](https://github.com/martinRenou))
- Update README [#8](https://github.com/jupyterlite/jupyterlite-sphinx/pull/8) ([@martinRenou](https://github.com/martinRenou))
- Add basic CI [#7](https://github.com/jupyterlite/jupyterlite-sphinx/pull/7) ([@martinRenou](https://github.com/martinRenou))
- Fix missing options_spec in Retrolite directive [#6](https://github.com/jupyterlite/jupyterlite-sphinx/pull/6) ([@martinRenou](https://github.com/martinRenou))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2022-02-28&to=2022-03-02&type=c))

[@martinRenou](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3AmartinRenou+updated%3A2022-02-28..2022-03-02&type=Issues) | [@psychemedia](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3Apsychemedia+updated%3A2022-02-28..2022-03-02&type=Issues)

## 0.3.0

([full changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/999dffa...d781ca9))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2022-02-25&to=2022-02-28&type=c))

## 0.2.0

([full changelog](https://github.com/jupyterlite/jupyterlite-sphinx/compare/e5aacec...999dffa))

### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterlite/jupyterlite-sphinx/graphs/contributors?from=2022-01-04&to=2022-02-25&type=c))

[@martinRenou](https://github.com/search?q=repo%3Ajupyterlite%2Fjupyterlite-sphinx+involves%3AmartinRenou+updated%3A2022-01-04..2022-02-25&type=Issues)
