"""mergedeep test module"""
import inspect
import unittest
from copy import deepcopy
from inspect import getmembers
from unittest.mock import patch

from mergedeep import merge, Strategy


class test_mergedeep(unittest.TestCase):
    """mergedeep function tests."""

    ##############################################################################################################################
    # REPLACE
    ##############################################################################################################################

    def test_should_merge_3_dicts_into_new_dict_using_replace_strategy_and_only_mutate_target(
        self
    ):
        expected = {
            "a": {"b": {"c": 5, "_c": 15}, "B": {"C": 10}},
            "d": 3,
            "e": {1: 2, "a": {"f": 2}},
            "f": [4, 5, 6],
        }

        a = {"a": {"b": {"c": 5}}, "d": 1, "e": {2: 3}, "f": [1, 2, 3]}
        a_copy = deepcopy(a)

        b = {"a": {"B": {"C": 10}}, "d": 2, "e": 2, "f": [4, 5, 6]}
        b_copy = deepcopy(b)

        c = {"a": {"b": {"_c": 15}}, "d": 3, "e": {1: 2, "a": {"f": 2}}}
        c_copy = deepcopy(c)

        actual = merge({}, a, b, c, strategy=Strategy.REPLACE)

        self.assertEqual(actual, expected)
        self.assertEqual(a, a_copy)
        self.assertEqual(b, b_copy)
        self.assertEqual(c, c_copy)

    def test_should_merge_2_dicts_into_existing_dict_using_replace_strategy_and_only_mutate_target(
        self
    ):
        expected = {
            "a": {"b": {"c": 5, "_c": 15}, "B": {"C": 10}},
            "d": 3,
            "e": {1: 2, "a": {"f": 2}},
            "f": [4, 5, 6],
        }

        a = {"a": {"b": {"c": 5}}, "d": 1, "e": {2: 3}, "f": [1, 2, 3]}
        a_copy = deepcopy(a)

        b = {"a": {"B": {"C": 10}}, "d": 2, "e": 2, "f": [4, 5, 6]}
        b_copy = deepcopy(b)

        c = {"a": {"b": {"_c": 15}}, "d": 3, "e": {1: 2, "a": {"f": 2}}}
        c_copy = deepcopy(c)

        actual = merge(a, b, c, strategy=Strategy.REPLACE)

        self.assertEqual(actual, expected)
        self.assertEqual(actual, a)
        self.assertNotEqual(a, a_copy)
        self.assertEqual(b, b_copy)
        self.assertEqual(c, c_copy)

    def test_should_have_default_strategy_of_replace(self):
        func_spec = inspect.getfullargspec(merge)
        default_strategy = Strategy.REPLACE

        self.assertEqual(func_spec.kwonlydefaults.get("strategy"), default_strategy)

        # mock_merge.method.assert_called_with(target, source, strategy=Strategy.REPLACE)

        ##############################################################################################################################
        # ADDITIVE
        ##############################################################################################################################

    def test_should_merge_3_dicts_into_new_dict_using_additive_strategy_on_lists_and_only_mutate_target(
        self
    ):
        expected = {
            "a": {"b": {"c": 5, "_c": 15}, "B": {"C": 10}},
            "d": 3,
            "e": {1: 2, "a": {"f": 2}},
            "f": [1, 2, 3, 4, 5, 6],
        }

        a = {"a": {"b": {"c": 5}}, "d": 1, "e": {2: 3}, "f": [1, 2, 3]}
        a_copy = deepcopy(a)

        b = {"a": {"B": {"C": 10}}, "d": 2, "e": 2, "f": [4, 5, 6]}
        b_copy = deepcopy(b)

        c = {"a": {"b": {"_c": 15}}, "d": 3, "e": {1: 2, "a": {"f": 2}}}
        c_copy = deepcopy(c)

        actual = merge({}, a, b, c, strategy=Strategy.ADDITIVE)

        self.assertEqual(actual, expected)
        self.assertEqual(a, a_copy)
        self.assertEqual(b, b_copy)
        self.assertEqual(c, c_copy)

    def test_should_merge_3_dicts_into_new_dict_using_additive_strategy_on_sets_and_only_mutate_target(
        self
    ):
        expected = {
            "a": {"b": {"c": 5, "_c": 15}, "B": {"C": 10}},
            "d": 3,
            "e": {1: 2, "a": {"f": 2}},
            "f": {1, 2, 3, 4, 5, 6},
        }

        a = {"a": {"b": {"c": 5}}, "d": 1, "e": {2: 3}, "f": {1, 2, 3}}
        a_copy = deepcopy(a)

        b = {"a": {"B": {"C": 10}}, "d": 2, "e": 2, "f": {4, 5, 6}}
        b_copy = deepcopy(b)

        c = {"a": {"b": {"_c": 15}}, "d": 3, "e": {1: 2, "a": {"f": 2}}}
        c_copy = deepcopy(c)

        actual = merge({}, a, b, c, strategy=Strategy.ADDITIVE)

        self.assertEqual(actual, expected)
        self.assertEqual(a, a_copy)
        self.assertEqual(b, b_copy)
        self.assertEqual(c, c_copy)

    ##############################################################################################################################
    # TYPESAFE
    ##############################################################################################################################

    def test_should_raise_TypeError_using_typesafe_strategy_if_types_differ(self):
        expected = {
            "a": {"b": {"c": 5, "_c": 15}, "B": {"C": 10}},
            "d": 3,
            "e": {1: 2, "a": {"f": 2}},
            "f": [4, 5, 6],
        }

        a = {"a": {"b": {"c": 5}}, "d": 1, "e": {2: 3}, "f": [1, 2, 3]}
        b = {"a": {"B": {"C": 10}}, "d": 2, "e": 2, "f": [4, 5, 6]}
        c = {"a": {"b": {"_c": 15}}, "d": 3, "e": {1: 2, "a": {"f": 2}}}

        with self.assertRaises(TypeError):
            merge({}, a, b, c, strategy=Strategy.TYPESAFE)

    def test_should_merge_3_dicts_into_new_dict_using_typesafe_strategy_and_only_mutate_target_if_types_are_compatible(
        self
    ):
        expected = {
            "a": {"b": {"c": 5, "_c": 15}, "B": {"C": 10}},
            "d": 3,
            "f": [4, 5, 6],
        }

        a = {"a": {"b": {"c": 5}}, "d": 1, "f": [1, 2, 3]}
        a_copy = deepcopy(a)

        b = {"a": {"B": {"C": 10}}, "d": 2, "f": [4, 5, 6]}
        b_copy = deepcopy(b)

        c = {"a": {"b": {"_c": 15}}, "d": 3}
        c_copy = deepcopy(c)

        actual = merge({}, a, b, c, strategy=Strategy.TYPESAFE)

        self.assertEqual(actual, expected)
        self.assertEqual(a, a_copy)
        self.assertEqual(b, b_copy)
        self.assertEqual(c, c_copy)


if __name__ == "__main__":
    unittest.main()
