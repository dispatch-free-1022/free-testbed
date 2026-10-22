"""Helper for flattening nested lists."""

from typing import Any, List


def flatten(nested: list) -> list:
    """Flatten arbitrarily nested lists into a single new list.

    Only ``list`` instances are expanded. Every other item (strings, bytes,
    tuples, dicts, ``None``, ...) is kept as-is, in order. The input is not
    mutated. Iterative, so deep nesting does not raise ``RecursionError``.
    """
    result: List[Any] = []
    stack = [iter(nested)]
    while stack:
        for item in stack[-1]:
            if isinstance(item, list):
                stack.append(iter(item))
                break
            result.append(item)
        else:
            stack.pop()
    return result
