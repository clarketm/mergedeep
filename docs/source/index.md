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

.. image:: https://pepy.tech/badge/mergedeep
    :target: https://pepy.tech/project/mergedeep
    
```

**A deep merge function for 🐍.**

## Installation

```bash
$ pip install mergedeep
```

## Usage

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

MIT © [**Travis Clarke**](https://blog.travismclarke.com/)

