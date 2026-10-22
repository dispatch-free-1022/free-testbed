import unittest

from median import median


class MedianTests(unittest.TestCase):
    def test_odd_length(self):
        result = median([3, 1, 2])
        self.assertEqual(result, 2.0)
        self.assertIsInstance(result, float)

    def test_even_length(self):
        self.assertEqual(median([4, 1, 3, 2]), 2.5)

    def test_single_element(self):
        self.assertEqual(median([5.0]), 5.0)

    def test_unsorted_input_not_mutated(self):
        xs = [5, 2, 9, 1, 7]
        self.assertEqual(median(xs), 5.0)
        self.assertEqual(xs, [5, 2, 9, 1, 7])

    def test_negative_numbers(self):
        self.assertEqual(median([-5, -1, -3]), -3.0)
        self.assertEqual(median([-2, 2]), 0.0)

    def test_floats(self):
        self.assertEqual(median([1.5, 2.5, 3.5, 4.5]), 3.0)

    def test_duplicates(self):
        self.assertEqual(median([2, 2, 2, 2]), 2.0)
        self.assertEqual(median([1, 2, 2, 3, 9]), 2.0)

    def test_empty_list_raises(self):
        with self.assertRaises(ValueError):
            median([])


if __name__ == "__main__":
    unittest.main()
