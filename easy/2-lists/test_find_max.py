from find_max import maxn


def test_empty():
    assert maxn([], n=3) is None


def test_find_max_one_element():
    assert maxn([2], n=2) == 2


def test_find_max_no_element_matching():
    assert maxn([1,2,3,4], n=5) is None


def test_find_max_find_correct_max_for_multiple_divisible_elements():
    assert maxn([2,4,6,8,10], n=2) == 10


def test_find_max_sequence():
    assert maxn([1,2,3,4,5,6,7,8,9,10], n=3) == 9
