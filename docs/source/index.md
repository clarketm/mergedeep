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
merge(destination: MutableMapping, *sources: Mapping, strategy: Strategy = Strategy.REPLACE) -> MutableMapping
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

> `Strategy.REPLACE`

```python3
# When `destination` and `source` keys are the same, replace the `destination` value with one from `source` (default).

# Note: with multiple sources, the `last` (i.e. rightmost) source value will be what appears in the merged result. 

from mergedeep import merge, Strategy

dst = {"key": [1, 2]}
src = {"key": [3, 4]}

merge(dst, src, strategy=Strategy.REPLACE) 
# same as: merge(dst, src)

print(dst)
# {"key": [3, 4]}
```

* Additive

> `Strategy.ADDITIVE`

```python3
# When `destination` and `source` values are both the same additive collection type, extend `destination` by adding values from `source`.
# Additive collection types include: `list`, `tuple`, `set`, and `Counter`

# Note: if the values are not additive collections of the same type, then fallback to a `REPLACE` merge.

from mergedeep import merge, Strategy

dst = {"key": [1, 2], "count": Counter({"a": 1, "b": 1})}
src = {"key": [3, 4], "count": Counter({"a": 1, "c": 1})}

merge(dst, src, strategy=Strategy.ADDITIVE) 

print(dst)
# {"key": [1, 2, 3, 4], "count": Counter({"a": 2, "b": 1, "c": 1})}
```

* Typesafe replace

> `Strategy.TYPESAFE_REPLACE` or `Strategy.TYPESAFE`

```python3
# When `destination` and `source` values are of different types, raise `TypeError`. Otherwise, perform a `REPLACE` merge.

from mergedeep import merge, Strategy

dst = {"key": [1, 2]}
src = {"key": {3, 4}}

merge(dst, src, strategy=Strategy.TYPESAFE_REPLACE) # same as: `Strategy.TYPESAFE`  
# TypeError: destination type: <class 'list'> differs from source type: <class 'set'> for key: "key"
```

* Typesafe additive

> `Strategy.TYPESAFE_ADDITIVE`

```python3
# When `destination` and `source` values are of different types, raise `TypeError`. Otherwise, perform a `ADDITIVE` merge.

from mergedeep import merge, Strategy

dst = {"key": [1, 2]}
src = {"key": {3, 4}}

merge(dst, src, strategy=Strategy.TYPESAFE_ADDITIVE) 
# TypeError: destination type: <class 'list'> differs from source type: <class 'set'> for key: "key"
```

## License

MIT © [**Travis Clarke**](https://blog.travismclarke.com/)

