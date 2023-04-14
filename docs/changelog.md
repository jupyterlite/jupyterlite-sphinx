# Changelog

<!-- <START NEW CHANGELOG ENTRY> -->

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

<!-- <END NEW CHANGELOG ENTRY> -->

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
