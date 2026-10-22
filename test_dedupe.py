from dedupe import dedupe


def test_empty():
    assert dedupe([]) == []


def test_removes_duplicates_keeping_order():
    assert dedupe([1, 2, 1, 3, 2]) == [1, 2, 3]


def test_all_unique_returns_new_list():
    items = [1, 2, 3]
    result = dedupe(items)
    assert result == [1, 2, 3]
    assert result is not items


def test_all_identical():
    assert dedupe([7, 7, 7, 7]) == [7]


def test_strings():
    assert dedupe(["b", "a", "b", "c", "a"]) == ["b", "a", "c"]


def test_mixed_hashable_types():
    assert dedupe([1, "1", 1, "1", None, None, (1, 2), (1, 2)]) == [
        1,
        "1",
        None,
        (1, 2),
    ]


def test_unhashable_items():
    assert dedupe([[1], [1], {"a": 1}, {"a": 1}]) == [[1], {"a": 1}]


def test_mixed_hashable_and_unhashable():
    items = [1, [1], 2, [1], 1, {"a": 1}, 2, {"a": 1}, [2]]
    assert dedupe(items) == [1, [1], 2, {"a": 1}, [2]]


def test_equal_values_keep_first_seen():
    assert dedupe([1, 1.0, True]) == [1]
    assert dedupe([True, 1]) == [True]


def test_input_not_mutated():
    items = [1, 2, 1, [3], [3]]
    snapshot = list(items)
    result = dedupe(items)
    assert items == snapshot
    assert result is not items
