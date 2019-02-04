"""mergedeep test module"""
import unittest
from copy import deepcopy

from mergedeep import merge


class test_mergedeep(unittest.TestCase):
    """mergedeep function tests."""

    def test_should_merge_3_dicts_into_new_dict_and_only_mutate_target(self):
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

        actual = merge({}, a, b, c)

        self.assertEqual(actual, expected)
        self.assertEqual(a, a_copy)
        self.assertEqual(b, b_copy)
        self.assertEqual(c, c_copy)

    def test_should_merge_2_dicts_into_existing_dict_and_only_mutate_target(self):
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

        actual = merge(a, b, c)

        self.assertEqual(actual, expected)
        self.assertEqual(actual, a)
        self.assertNotEqual(a, a_copy)
        self.assertEqual(b, b_copy)
        self.assertEqual(c, c_copy)


if __name__ == "__main__":
    unittest.main()
