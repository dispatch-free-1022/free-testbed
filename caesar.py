"""Caesar cipher helper."""


def shift(text: str, k: int) -> str:
    """Rotate ASCII letters in ``text`` by ``k`` positions.

    Case is preserved. Characters other than ``A-Z`` and ``a-z`` (digits,
    punctuation, whitespace, non-ASCII letters) are left unchanged. ``k`` may
    be negative or larger than 26.
    """
    result = []
    for c in text:
        if "a" <= c <= "z":
            result.append(chr((ord(c) - ord("a") + k) % 26 + ord("a")))
        elif "A" <= c <= "Z":
            result.append(chr((ord(c) - ord("A") + k) % 26 + ord("A")))
        else:
            result.append(c)
    return "".join(result)
