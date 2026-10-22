import unittest

from roman import to_roman


def _from_roman(s: str) -> int:
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for i, ch in enumerate(s):
        v = values[ch]
        if i + 1 < len(s) and values[s[i + 1]] > v:
            total -= v
        else:
            total += v
    return total


class ToRomanTest(unittest.TestCase):
    def test_known_values(self):
        cases = {
            1: "I",
            4: "IV",
            9: "IX",
            14: "XIV",
            40: "XL",
            90: "XC",
            400: "CD",
            1994: "MCMXCIV",
            2024: "MMXXIV",
        }
        for n, expected in cases.items():
            with self.subTest(n=n):
                self.assertEqual(to_roman(n), expected)

    def test_boundaries(self):
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_out_of_range(self):
        for n in (0, -1, 4000):
            with self.subTest(n=n):
                with self.assertRaises(ValueError):
                    to_roman(n)

    def test_non_int(self):
        for n in ("5", 3.5, None, True):
            with self.subTest(n=n):
                with self.assertRaises(ValueError):
                    to_roman(n)

    def test_round_trip(self):
        for n in range(1, 4000):
            self.assertEqual(_from_roman(to_roman(n)), n)


if __name__ == "__main__":
    unittest.main()
