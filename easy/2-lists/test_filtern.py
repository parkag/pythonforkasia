from filtern import filter_n

def test_filter_empty():
    assert filter_n([], n=10) == []


def test_filter_by_10():
    assert filter_n([5,10,15,20], n=10) == [10, 20]


def test_filter_by_7():
    assert filter_n([1,2,3,4,5,6,7,21,22,140], n=7) == [7,21,140]


def test_filter_by_0():
    assert filter_n([1,2,3,4,5], n=0) == []


def test_filter_zero():
    assert filter_n([0,1,2,3], n=2) == [0,2]


def test_filter_negative():
    assert filter_n([0,-1,-2,-3,-4], n=2) == [0, -2, -4]


def test_filter_by_negative():
    assert filter_n([1,2,3,4], n=-2) == [2,4]

