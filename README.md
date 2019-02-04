# [mergedeep](https://mergedeep.readthedocs.io/en/latest/)

[![PyPi release](https://img.shields.io/pypi/v/mergedeep.svg)](https://pypi.org/project/mergedeep/)
[![Downloads](https://pepy.tech/badge/mergedeep)](https://pepy.tech/project/mergedeep)
[![Documentation Status](https://readthedocs.org/projects/mergedeep/badge/?version=latest)](https://mergedeep.readthedocs.io/en/latest/?badge=latest)

A deep merge function for 🐍.

[Check out the mergedeep docs](https://mergedeep.readthedocs.io/en/latest/)

## Installation

```bash
$ pip install mergedeep
```

## Usage

```text
merge(target: Map[KT, VT], *sources: Map[KT, VT]) -> Map[KT, VT]
```

Deep merge without mutating the source dicts.

```python
from mergedeep import merge

a = {"keyA": 1}
b = {"keyB": {"sub1": 10}}
c = {"keyB": {"sub2": 20}}

merged = merge({}, a, b, c) 

print(merged)
# {"keyA": 1, "keyB": {"sub1": 10, "sub2": 20}}
```

Deep merge into an existing dict.
```python
from mergedeep import merge

a = {"keyA": 1}
b = {"keyB": {"sub1": 10}}
c = {"keyB": {"sub2": 20}}

merge(a, b, c) 

print(a)
# {"keyA": 1, "keyB": {"sub1": 10, "sub2": 20}}
```

## License

MIT &copy; [**Travis Clarke**](https://blog.travismclarke.com/)
