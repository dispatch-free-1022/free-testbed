import pytest

from words import word_count


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello world", 2),
        ("hello", 1),
        ("", 0),
        ("   ", 0),
        ("\n\t ", 0),
        ("  leading and trailing  ", 3),
        ("multiple   spaces   between", 3),
        ("tabs\tand\nnewlines", 3),
        ("one, two. three!", 3),
    ],
)
def test_word_count(text, expected):
    assert word_count(text) == expected
