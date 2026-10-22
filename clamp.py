def clamp(x: float, lo: float, hi: float) -> float:
    """Return ``x`` limited to the inclusive range ``[lo, hi]``.

    Raises ValueError if ``lo`` is greater than ``hi``.
    """
    if lo > hi:
        raise ValueError(f"lo ({lo}) must not be greater than hi ({hi})")
    return max(lo, min(x, hi))
