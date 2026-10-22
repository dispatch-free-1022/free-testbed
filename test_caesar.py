import unittest

from caesar import shift


class ShiftTests(unittest.TestCase):
    def test_basic_lowercase(self):
        self.assertEqual(shift("abc", 1), "bcd")

    def test_basic_uppercase_wraps(self):
        self.assertEqual(shift("XYZ", 3), "ABC")

    def test_mixed_case_and_punctuation(self):
        self.assertEqual(shift("Hello, World!", 3), "Khoor, Zruog!")

    def test_non_letters_untouched(self):
        text = "123 \t\n.,;!?-_@#"
        self.assertEqual(shift(text, 5), text)

    def test_non_ascii_untouched(self):
        self.assertEqual(shift("é", 3), "é")
        self.assertEqual(shift("ß", 3), "ß")
        self.assertEqual(shift("aéb", 1), "béc")

    def test_zero_shift(self):
        text = "Hello, World! 123"
        self.assertEqual(shift(text, 0), text)

    def test_multiples_of_26(self):
        text = "Hello, World!"
        for k in (26, 52, -26, -52):
            self.assertEqual(shift(text, k), text)

    def test_k_greater_than_26(self):
        self.assertEqual(shift("abc", 27), "bcd")

    def test_negative_k(self):
        self.assertEqual(shift("bcd", -1), "abc")

    def test_large_negative_k(self):
        self.assertEqual(shift("abc", -27), "zab")

    def test_empty_string(self):
        self.assertEqual(shift("", 5), "")

    def test_round_trip(self):
        text = "The Quick Brown Fox, jumps over 13 lazy dogs! é"
        for k in (-100, -27, -1, 0, 1, 13, 25, 26, 99):
            self.assertEqual(shift(shift(text, k), -k), text)


if __name__ == "__main__":
    unittest.main()
