from filter2 import filter_two


def test_filter2_empty():
    assert filter_two([]) == []


def test_filter2_simple():
    assert filter_two([1,2,3,4]) == [2,4]


def test_filter2_not_divisible():
    assert filter_two([1,3,5,7]) == []


def test_filter2_multiple():
    assert filter_two([1,2,2,3,4,5,6,99990]) == [2,2,4,6,99990]


def test_filter2_zero():
    assert filter_two([0]) == [0]


def test_filter2_negative():
    assert filter_two([-1,-2,-3,-4,-5,-6]) == [-2,-4,-6]

