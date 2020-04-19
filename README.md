# [mergedeep](https://mergedeep.readthedocs.io/en/latest/)

[![PyPi release](https://img.shields.io/pypi/v/mergedeep.svg)](https://pypi.org/project/mergedeep/)
[![PyPi versions](https://img.shields.io/pypi/pyversions/mergedeep.svg)](https://pypi.org/project/mergedeep/)
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
merge(target: Map[KT, VT], *sources: Map[KT, VT], strategy: Strategy = Strategy.REPLACE) -> Map[KT, VT]
```

Deep merge without mutating the source dicts.

```python3
from mergedeep import merge

a = {"keyA": 1}
b = {"keyB": {"sub1": 10}}
c = {"keyB": {"sub2": 20}}

merged = merge({}, a, b, c) 

print(merged)
# {"keyA": 1, "keyB": {"sub1": 10, "sub2": 20}}
```

Deep merge into an existing dict.
```python3
from mergedeep import merge

a = {"keyA": 1}
b = {"keyB": {"sub1": 10}}
c = {"keyB": {"sub2": 20}}

merge(a, b, c) 

print(a)
# {"keyA": 1, "keyB": {"sub1": 10, "sub2": 20}}
```

### Merge strategies:
1. Replace (*default*)
```python3
# Strategy.REPLACE
# When `target` and `source` values are the same, replace the `target` value with one from `source` (default).
# Note: with multiple sources, the `last` source value will be what appears in the merged result. 

from mergedeep import merge, Strategy

target = {"key": [1, 2]}
source = {"key": [3, 4]}

merge(target, source, strategy=Strategy.REPLACE) 
# same as: merge(target, source)

print(target)
# {"key": [3, 4]}
```

2. Additive
```python3
# Strategy.ADDITIVE
# When `target` and `source` values are both either `list`, `tuple`, or `set`, extend/update `target` with values from `source` collection.

from mergedeep import merge, Strategy

target = {"key": [1, 2]}
source = {"key": [3, 4]}

merge(target, source, strategy=Strategy.ADDITIVE) 

print(target)
# {"key": [1, 2, 3, 4]}
```

3. Typesafe replace
```python3
# Strategy.TYPESAFE_REPLACE or Strategy.TYPESAFE 
# When `target` and `source` values are of different types, raise `TypeError`. Otherwise, perform a `REPLACE` merge.

from mergedeep import merge, Strategy

target = {"key": [1, 2]}
source = {"key": {3, 4}}

merge(target, source, strategy=Strategy.TYPESAFE_REPLACE) # or `Strategy.TYPESAFE`  
# TypeError: target type: <class 'list'> differs from source type: <class 'set'> for key: "key"
```

4. Typesafe additive
```python3
# Strategy.TYPESAFE_ADDITIVE
# When `target` and `source` values are of different types, raise `TypeError`. Otherwise, perform a `ADDITIVE` merge.

from mergedeep import merge, Strategy

target = {"key": [1, 2]}
source = {"key": {3, 4}}

merge(target, source, strategy=Strategy.TYPESAFE_ADDITIVE) 
# TypeError: target type: <class 'list'> differs from source type: <class 'set'> for key: "key"
```

## License

MIT &copy; [**Travis Clarke**](https://blog.travismclarke.com/)
