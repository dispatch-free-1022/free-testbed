def chunk(items: list, size: int) -> list[list]:
    """Split ``items`` into consecutive lists of at most ``size`` items.

    The last chunk may be shorter than ``size``. The input list is not
    modified and the returned chunks are new lists.

    Raises:
        ValueError: if ``size`` is less than 1.
    """
    if size < 1:
        raise ValueError("size must be >= 1")
    return [items[i:i + size] for i in range(0, len(items), size)]
