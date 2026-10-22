import unittest

from chunk import chunk


class ChunkTest(unittest.TestCase):
    def test_even_split(self):
        self.assertEqual(chunk([1, 2, 3, 4], 2), [[1, 2], [3, 4]])

    def test_last_chunk_shorter(self):
        self.assertEqual(chunk([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])

    def test_empty_list(self):
        self.assertEqual(chunk([], 3), [])

    def test_size_larger_than_list(self):
        self.assertEqual(chunk([1, 2], 5), [[1, 2]])

    def test_size_one(self):
        self.assertEqual(chunk([1, 2, 3], 1), [[1], [2], [3]])

    def test_size_zero_raises(self):
        with self.assertRaises(ValueError):
            chunk([1, 2, 3], 0)

    def test_negative_size_raises(self):
        with self.assertRaises(ValueError):
            chunk([1, 2, 3], -1)

    def test_input_not_mutated(self):
        items = [1, 2, 3, 4, 5]
        chunk(items, 2)
        self.assertEqual(items, [1, 2, 3, 4, 5])

    def test_chunks_are_new_lists(self):
        items = [1, 2]
        result = chunk(items, 5)
        self.assertIsNot(result[0], items)
        result[0].append(3)
        self.assertEqual(items, [1, 2])


if __name__ == "__main__":
    unittest.main()
