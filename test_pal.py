import pytest

from pal import is_palindrome


def test_empty_string():
    assert is_palindrome("") is True


def test_single_character():
    assert is_palindrome("a") is True


@pytest.mark.parametrize(
    "text",
    [
        "racecar",
        "RaceCar",
        "A man, a plan, a canal: Panama",
        "No 'x' in Nixon",
        "12321",
        "ßss",
        "İ",
        "!!!",
        " ",
    ],
)
def test_palindromes(text):
    assert is_palindrome(text) is True


@pytest.mark.parametrize(
    "text",
    [
        "hello",
        "ab",
        "12345",
        "a1b",
    ],
)
def test_non_palindromes(text):
    assert is_palindrome(text) is False
