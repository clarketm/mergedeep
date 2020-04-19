```eval_rst
.. meta::
   :description: mergedeep: A deep merge function for 🐍.

.. title:: mergedeep
```

# [mergedeep](https://pypi.org/project/mergedeep/)

```eval_rst
Version |version|

.. image:: https://img.shields.io/pypi/v/mergedeep.svg
    :target: https://pypi.org/project/mergedeep/

.. image:: https://img.shields.io/pypi/pyversions/mergedeep.svg
    :target: https://pypi.org/project/mergedeep/
    
.. image:: https://pepy.tech/badge/mergedeep
    :target: https://pepy.tech/project/mergedeep
    
```

**A deep merge function for 🐍.**

## Installation

```bash
$ pip install mergedeep
```

## Usage

```text
merge(destination: Map[KT, VT], *sources: Map[KT, VT], strategy: Strategy = Strategy.REPLACE) -> Map[KT, VT]
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
* Replace (*default*)
```python3
# Strategy.REPLACE
# When `destination` and `source` values are the same, replace the `destination` value with one from `source` (default).
# Note: with multiple sources, the `last` source value will be what appears in the merged result. 

from mergedeep import merge, Strategy

dst = {"key": [1, 2]}
src = {"key": [3, 4]}

merge(dst, src, strategy=Strategy.REPLACE) 
# same as: merge(dst, src)

print(dst)
# {"key": [3, 4]}
```

* Additive
```python3
# Strategy.ADDITIVE
# When `destination` and `source` values are both either `list`, `tuple`, or `set`, extend/update `destination` with values from `source` collection.

from mergedeep import merge, Strategy

dst = {"key": [1, 2]}
src = {"key": [3, 4]}

merge(dst, src, strategy=Strategy.ADDITIVE) 

print(dst)
# {"key": [1, 2, 3, 4]}
```

* Typesafe replace
```python3
# Strategy.TYPESAFE_REPLACE or Strategy.TYPESAFE 
# When `destination` and `source` values are of different types, raise `TypeError`. Otherwise, perform a `REPLACE` merge.

from mergedeep import merge, Strategy

dst = {"key": [1, 2]}
src = {"key": {3, 4}}

merge(dst, src, strategy=Strategy.TYPESAFE_REPLACE) # same as: `Strategy.TYPESAFE`  
# TypeError: destination type: <class 'list'> differs from source type: <class 'set'> for key: "key"
```

* Typesafe additive
```python3
# Strategy.TYPESAFE_ADDITIVE
# When `destination` and `source` values are of different types, raise `TypeError`. Otherwise, perform a `ADDITIVE` merge.

from mergedeep import merge, Strategy

dst = {"key": [1, 2]}
src = {"key": {3, 4}}

merge(dst, src, strategy=Strategy.TYPESAFE_ADDITIVE) 
# TypeError: destination type: <class 'list'> differs from source type: <class 'set'> for key: "key"
```

## License

MIT © [**Travis Clarke**](https://blog.travismclarke.com/)

