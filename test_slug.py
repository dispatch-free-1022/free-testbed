import pytest

from slug import slugify


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello World", "hello-world"),
        ("Hello, World!", "hello-world"),
        ("  Hello   World  ", "hello-world"),
        ("Caf\u00e9 Ol\u00e9", "caf\u00e9-ol\u00e9"),
        ("", ""),
        ("!!!", ""),
        ("a_b", "a-b"),
        ("Foo--Bar", "foo-bar"),
        ("Python 3 rocks", "python-3-rocks"),
    ],
    ids=[
        "plain-words",
        "punctuation",
        "repeated-spaces",
        "accents-kept",
        "empty-string",
        "only-punctuation",
        "underscore",
        "repeated-hyphens",
        "digits",
    ],
)
def test_slugify(text, expected):
    assert slugify(text) == expected
