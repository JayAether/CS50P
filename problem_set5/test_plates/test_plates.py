from plates import is_valid


def test_length():
    assert is_valid('d') == False
    assert is_valid('dDHHjjjcjcj') == False


def test_first():
    assert is_valid('a') == False
    assert is_valid('1') == False
    assert is_valid('a2dd') == False
    assert is_valid('22ddf') == False


def test_capital():
    assert is_valid('ABC') == True
    assert is_valid('TEST2') == True


def test_minor():
    assert is_valid('fafs') == True
    assert is_valid('if10') == True


def test_digits():
    assert is_valid('pp42') == True
    assert is_valid('2222') == False
    assert is_valid('af4f') == False
    assert is_valid('3jfj') == False
    assert is_valid('oaj04') == False


def test_special_characters():
    assert is_valid('fs Msf') == False
    assert is_valid('no,why') == False
    assert is_valid('..what') == False
    assert is_valid('') == False
    assert is_valid(' ') == False


