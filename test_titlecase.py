import pytest

from titlecase import title_case


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("the lord of the rings", "The Lord of the Rings"),
        ("a tale of two cities", "A Tale of Two Cities"),
        ("THE END OF AN ERA", "The End of an Era"),
        ("", ""),
        ("hello", "Hello"),
        ("of mice and men", "Of Mice And Men"),
        ("  the  cat ", "  The  Cat "),
        ("  the cat", "  The Cat"),
        ("Cat Of The Year", "Cat of the Year"),
        ("the cat\nthe dog", "The Cat\nthe Dog"),
        ("hello\tworld", "Hello\tWorld"),
        ("cat\nof mice", "Cat\nof Mice"),
    ],
)
def test_title_case(text, expected):
    assert title_case(text) == expected
