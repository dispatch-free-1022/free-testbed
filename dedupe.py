"""Helper for removing duplicates from a list while keeping order."""


def dedupe(items: list) -> list:
    """Return a new list with duplicates removed, keeping first-seen order.

    Hashable items are tracked in a set. Unhashable items (such as lists or
    dicts) fall back to a linear ``==`` comparison, which is O(n^2) for them.

    Items are compared with ``==``/hash semantics, so values that are equal
    (for example ``1``, ``1.0`` and ``True``) count as duplicates and only the
    first one seen is kept. The input list is not modified.
    """
    seen = set()
    seen_unhashable = []
    result = []
    for item in items:
        try:
            if item in seen:
                continue
            seen.add(item)
        except TypeError:
            if item in seen_unhashable:
                continue
            seen_unhashable.append(item)
        result.append(item)
    return result
