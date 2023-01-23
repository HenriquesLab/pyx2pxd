# pyx2pxd


Simple library to auto generate pxd files from pyx by extracting function and class signatures. <br>
Initially developed to aid in the [NanoPyx](https://github.com/HenriquesLab/NanoPyx) project.

---


## Installation

You can install `pyx2pxd` via [pip]:

```shell
pip install pyx2pxd
```

## Usage

```shell
pyx2pxd folder_path_to_process
```

*Note*: pyx2pxd will only analyze pyx files that contain the comment <code># cython: autogen_pxd=True</code>. For example:

```code
# cython: infer_types=True, wraparound=False, nonecheck=False, boundscheck=False, cdivision=True, language_level=3, profile=True, autogen_pxd=True

from libc.math cimport fabs
...
```

## License

Distributed under the terms of the [GNU GPL v2.0] license,
"pyx2pxd" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[file an issue]: https://github.com/HenriquesLab/NanoPyx/issues
[pip]: https://pypi.org/project/pip/
[pypi]: https://pypi.org/
