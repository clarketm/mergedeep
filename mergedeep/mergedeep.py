from collections.abc import Mapping
from copy import deepcopy
from enum import Enum
from functools import reduce
from typing import TypeVar, MutableMapping as Map

KT = TypeVar("KT")
VT = TypeVar("VT")


class Strategy(Enum):
    # Replace `target` item with one from `source` (default).
    REPLACE = 0
    # Combined `list` or `set` types into one collection.
    ADDITIVE = 1
    # Raise `TypeError` when `target` and `source` types differ.
    TYPESAFE = 2


def _handle_merge_replace(target, source, key):
    # If a key exists in both objects and the values are `different`, the value from the `source` object will be used.
    target[key] = source[key]


def _handle_merge_additive(target, source, key):
    # List and Set values are combined into one long collection.
    if isinstance(target[key], list) and isinstance(source[key], list):
        # Extend target if both target and source are `list` type.
        target[key].extend(source[key])
    elif isinstance(target[key], set) and isinstance(source[key], set):
        # Update target if both target and source are `set` type.
        target[key].update(source[key])
    else:
        _handle_merge[Strategy.REPLACE](target, source, key)


def _handle_merge_typesafe(target, source, key):
    # Raise a TypeError if the target and source types differ.
    if type(target[key]) is not type(source[key]):
        raise TypeError(
            f'target type: {type(target[key])} differs from source type: {type(source[key])} for key: "{key}"'
        )
    else:
        _handle_merge[Strategy.REPLACE](target, source, key)


_handle_merge = {
    Strategy.REPLACE: _handle_merge_replace,
    Strategy.ADDITIVE: _handle_merge_additive,
    Strategy.TYPESAFE: _handle_merge_typesafe,
}


def merge(
    target: Map[KT, VT], *sources: Map[KT, VT], strategy: Strategy = Strategy.REPLACE
) -> Map[KT, VT]:
    """
    A deep merge function for 🐍.

    :param target: Map[KT, VT]:
    :param *sources: Map[KT, VT]:
    :param strategy: Strategy (Default: Strategy.REPLACE):
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
                    _handle_merge.get(strategy, Strategy.REPLACE)(
                        target, deepcopy(source), key
                    )
            else:
                # If the key exists only in `source`, the value from the `source` object will be used.
                target[key] = deepcopy(source[key])
        return target

    return reduce(_deepmerge, sources, target)
