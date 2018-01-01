from draw_tree import draw_tree


def test_level_0():
    assert draw_tree(0) == '|__|'


def test_level_1():
    tree = '''
  /\
 /  \
/____\
 |__|
'''
    assert draw_tree(1) == tree


def test_level_2():
    tree = '''
  /\
 /  \
/_  _\
 /  \
/____\
 |__|
'''
    assert draw_tree(2) == tree


def test_level_3():
    tree = '''
  /\
 /  \
/_  _\
 /  \
/_  _\
 /  \
/____\
 |__|
'''
    assert draw_tree(3) == tree


def test_level_10():
    top = '''
  /\
 /  \
/_  _\
'''
    segment = '''
 /  \
/_  _\
'''
    bottom = '''
 /  \
/____\
 |__|
'''
    tree = top + segment * 9 + bottom
    assert draw_tree(10) == tree

