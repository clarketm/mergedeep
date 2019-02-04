from collections.abc import Mapping
from copy import deepcopy
from functools import reduce
from typing import TypeVar, MutableMapping as Map

KT = TypeVar("KT")
VT = TypeVar("VT")


def merge(target: Map[KT, VT], *sources: Map[KT, VT]) -> Map[KT, VT]:
    """
    A deep merge function for 🐍.

    :param target: Map[KT, VT]:
    :param *sources: Map[KT, VT]:
    """

    def _deepmerge(target: Map[KT, VT], source: Map[KT, VT]):
        """
        :param target: Map[KT, VT]:
        :param source: Map[KT, VT]:
        """
        for key in source:
            if key in target:
                if isinstance(target[key], Mapping) and isinstance(
                    source[key], Mapping
                ):
                    # If the key for both `target` and `source` are Mapping types, then recurse.
                    _deepmerge(target[key], source[key])
                elif target[key] == source[key]:
                    # If a key exists in both objects and the values are `same`, the value from the `target` object will be used.
                    pass
                else:
                    # If a key exists in both objects and the values are `different`, the value from the `source` object will be used.
                    target[key] = deepcopy(source[key])
            else:
                # If the key exists only in `source`, the value from the `source` object will be used.
                target[key] = deepcopy(source[key])
        return target

    return reduce(_deepmerge, sources, target)
