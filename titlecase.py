"""Title-casing helper."""

import re

_SMALL_WORDS = frozenset({"a", "an", "the", "of"})


def title_case(text: str) -> str:
    """Capitalise each word, keeping "a", "an", "the" and "of" lowercase.

    The small words are only capitalised when they are the first word.
    The rest of each word is lowercased, so "NASA" becomes "Nasa". Words are
    delimited by any whitespace (spaces, tabs, newlines) and the original
    whitespace is preserved. Hyphens and punctuation get no special handling:
    "word-word" becomes "Word-word".
    """
    result = []
    seen_word = False
    # The capturing group keeps the whitespace separators in the result.
    for token in re.split(r"(\s+)", text):
        if not token or token.isspace():
            result.append(token)
            continue
        if seen_word and token.lower() in _SMALL_WORDS:
            result.append(token.lower())
        else:
            result.append(token[:1].upper() + token[1:].lower())
        seen_word = True
    return "".join(result)
