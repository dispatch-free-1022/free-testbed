def median(xs: list[float]) -> float:
    """Return the median of ``xs`` as a float.

    For an even number of items, the mean of the two middle values is
    returned. The input list is not modified.

    Raises:
        ValueError: if ``xs`` is empty.
    """
    if not xs:
        raise ValueError("median() arg is an empty list")
    s = sorted(xs)
    n = len(s)
    mid = n // 2
    if n % 2:
        return float(s[mid])
    return (s[mid - 1] + s[mid]) / 2
