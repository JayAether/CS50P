from numb3rs import validate


def test_validate_true():
    assert validate('1.2.3.4') == True
    assert validate('122.22.0.68') == True
    assert validate("0.0.0.0") == True


def test_higher_num():
    assert validate('1232.24.322.822') == False
    assert validate("1.1.1.256") == False


def test_letters():
    assert validate('a.b.c.d') == False


def test_non_pattern():
    assert validate('cat') == False
    assert validate('12/a,as.4') == False
    assert validate("192.168.1.255.1") == False
    assert validate("192.168.1") == False
