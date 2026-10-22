def word_count(text: str) -> int:
    """Return the number of whitespace-separated words in ``text``.

    Empty and whitespace-only text counts as 0 words.
    """
    return len(text.split())
