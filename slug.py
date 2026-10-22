import re


def slugify(text: str) -> str:
    """Return a lowercase, hyphen-separated slug for ``text``.

    Every run of non-alphanumeric characters (including underscores) becomes a
    single hyphen, and leading/trailing hyphens are stripped. Accented letters
    are kept as letters.
    """
    return re.sub(r"[\W_]+", "-", text.lower()).strip("-")
