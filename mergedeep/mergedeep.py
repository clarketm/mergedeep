from collections.abc import Mapping
from copy import deepcopy
from enum import Enum
from functools import reduce, partial
from typing import TypeVar, MutableMapping as Map

KT = TypeVar("KT")
VT = TypeVar("VT")


class Strategy(Enum):
    # Replace `destination` item with one from `source` (default).
    REPLACE = 0
    # Combined `list`, `tuple`, or `set` types into one collection.
    ADDITIVE = 1
    # Alias to: `TYPESAFE_REPLACE`
    TYPESAFE = 2
    # Raise `TypeError` when `destination` and `source` types differ. Otherwise, perform a `REPLACE` merge.
    TYPESAFE_REPLACE = 3
    # Raise `TypeError` when `destination` and `source` types differ. Otherwise, perform a `ADDITIVE` merge.
    TYPESAFE_ADDITIVE = 4


def _handle_merge_replace(destination, source, key):
    # If a key exists in both objects and the values are `different`, the value from the `source` object will be used.
    destination[key] = deepcopy(source[key])


def _handle_merge_additive(destination, source, key):
    # List and Set values are combined into one long collection.
    if isinstance(destination[key], list) and isinstance(source[key], list):
        # Extend destination if both destination and source are `list` type.
        destination[key].extend(deepcopy(source[key]))
    elif isinstance(destination[key], set) and isinstance(source[key], set):
        # Update destination if both destination and source are `set` type.
        destination[key].update(deepcopy(source[key]))
    elif isinstance(destination[key], tuple) and isinstance(source[key], tuple):
        # Update destination if both destination and source are `tuple` type.
        destination[key] = destination[key] + deepcopy(source[key])
    else:
        _handle_merge[Strategy.REPLACE](destination, source, key)


def _handle_merge_typesafe(destination, source, key, strategy):
    # Raise a TypeError if the destination and source types differ.
    if type(destination[key]) is not type(source[key]):
        raise TypeError(
            f'destination type: {type(destination[key])} differs from source type: {type(source[key])} for key: "{key}"'
        )
    else:
        _handle_merge[strategy](destination, source, key)


_handle_merge = {
    Strategy.REPLACE: _handle_merge_replace,
    Strategy.ADDITIVE: _handle_merge_additive,
    Strategy.TYPESAFE: partial(_handle_merge_typesafe, strategy=Strategy.REPLACE),
    Strategy.TYPESAFE_REPLACE: partial(_handle_merge_typesafe, strategy=Strategy.REPLACE),
    Strategy.TYPESAFE_ADDITIVE: partial(_handle_merge_typesafe, strategy=Strategy.ADDITIVE),
}


def merge(destination: Map[KT, VT], *sources: Map[KT, VT], strategy: Strategy = Strategy.REPLACE,) -> Map[KT, VT]:
    """
    A deep merge function for 🐍.

    :param destination: Map[KT, VT]:
    :param *sources: Map[KT, VT]:
    :param strategy: Strategy (Default: Strategy.REPLACE):
    """

    def _deepmerge(destination: Map[KT, VT], source: Map[KT, VT]):
        """
        :param destination: Map[KT, VT]:
        :param source: Map[KT, VT]:
        """
        for key in source:
            if key in destination:
                if isinstance(destination[key], Mapping) and isinstance(source[key], Mapping):
                    # If the key for both `destination` and `source` are Mapping types, then recurse.
                    _deepmerge(destination[key], source[key])
                elif destination[key] == source[key]:
                    # If a key exists in both objects and the values are `same`, the value from the `destination` object will be used.
                    pass
                else:
                    _handle_merge.get(strategy, Strategy.REPLACE)(destination, source, key)
            else:
                # If the key exists only in `source`, the value from the `source` object will be used.
                destination[key] = deepcopy(source[key])
        return destination

    return reduce(_deepmerge, sources, destination)
