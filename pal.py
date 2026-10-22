def is_palindrome(text: str) -> bool:
    """Return True if ``text`` reads the same forwards and backwards.

    Case is ignored, as is every character for which ``str.isalnum()`` is
    False. A string with no alphanumeric characters counts as a palindrome.
    """
    # Casefold first, then filter: a fold can expand to several characters,
    # some of them non-alphanumeric (e.g. "İ" -> "i" + U+0307).
    cleaned = "".join(c for c in text.casefold() if c.isalnum())
    return cleaned == cleaned[::-1]
