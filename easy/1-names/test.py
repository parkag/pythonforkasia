from names import is_female

def test_female():
    assert is_female('Kasia') is True
    assert is_female('Marta') is True
    assert is_female('Magda') is True
    assert is_female('Karyna') is True
    assert is_female('Grażyna') is True

def test_male():
    assert is_female('Grzegorz') is False
    assert is_female('Zbigniew') is False
    assert is_female('Artur') is False
    assert is_female('Janusz') is False
    assert is_female('Sebastian') is False

