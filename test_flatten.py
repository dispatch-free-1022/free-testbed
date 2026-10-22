import copy
import unittest

from flatten import flatten


class FlattenTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(flatten([]), [])

    def test_already_flat_returns_new_list(self):
        data = [1, 2, 3]
        result = flatten(data)
        self.assertEqual(result, [1, 2, 3])
        self.assertIsNot(result, data)

    def test_nested(self):
        self.assertEqual(flatten([1, [2, [3, [4]]]]), [1, 2, 3, 4])

    def test_empty_nested_lists_vanish(self):
        self.assertEqual(flatten([[], [[]], 1]), [1])

    def test_strings_not_split(self):
        self.assertEqual(flatten(["ab", ["cd", ["e"]]]), ["ab", "cd", "e"])

    def test_mixed_types_preserved(self):
        d = {"a": [1]}
        self.assertEqual(
            flatten([None, (1, [2]), [d, b"xy"], 0, [[None]]]),
            [None, (1, [2]), d, b"xy", 0, None],
        )

    def test_deep_nesting(self):
        data = [1]
        for _ in range(5000):
            data = [data]
        self.assertEqual(flatten(data), [1])

    def test_input_not_mutated(self):
        data = [1, [2, [3, []]], "a"]
        expected = copy.deepcopy(data)
        flatten(data)
        self.assertEqual(data, expected)


if __name__ == "__main__":
    unittest.main()
