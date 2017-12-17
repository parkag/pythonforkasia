from unique import unique


def test_unique_empty():
    assert unique([]) == []


def test_unique_unique():
    assert unique([1,2,3,4,5]) == [1,2,3,4,5]


def test_unique_removes_duplicates():
    assert unique([1,1,2,2]) == [1,2]


def test_big_list_of_duplicates():
    assert unique([3] * 10000) == [3]

