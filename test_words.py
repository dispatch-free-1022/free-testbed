import pytest

from words import word_count


@pytest.mark.parametrize(
    "text, expected",
    [
        ("", 0),
        ("hello", 1),
        ("hello   world", 2),
        ("  a  b   c  ", 3),
        ("a\tb\nc", 3),
        ("   ", 0),
    ],
)
def test_word_count(text, expected):
    assert word_count(text) == expected
