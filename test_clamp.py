import pytest

from clamp import clamp


@pytest.mark.parametrize(
    "x, lo, hi, expected",
    [
        (5, 0, 10, 5),
        (-1, 0, 10, 0),
        (11, 0, 10, 10),
        (0, 0, 10, 0),
        (10, 0, 10, 10),
        (3, 4, 4, 4),
        (4, 4, 4, 4),
        (5, 4, 4, 4),
        (-5.5, -3.0, -1.0, -3.0),
        (-2.5, -3.0, -1.0, -2.5),
        (0.0, -3.0, -1.0, -1.0),
        (5, float("-inf"), float("inf"), 5),
        (-100, float("-inf"), 0, -100),
        (100, 0, float("inf"), 100),
    ],
)
def test_clamp_values(x, lo, hi, expected):
    assert clamp(x, lo, hi) == expected


@pytest.mark.parametrize("x", [-10, 5, 10, 20])
def test_clamp_raises_when_lo_greater_than_hi(x):
    with pytest.raises(ValueError, match="must not be greater than"):
        clamp(x, 10, 0)
