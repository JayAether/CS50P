from bank import value


def test_hellos():
    assert value('hello') == 0
    assert value('Hello,') == 0
    assert value('Hello?') == 0


def test_h_greetings():
    assert value('hi, i am...') == 20
    assert value('hya!') == 20
    assert value('HEY!!') == 20


def test_non_h_greetings():
    assert value('sup!') == 100
    assert value('according to all laws of aviation') == 100
    assert value('i pissed on the moon') == 100


def test_num():
    assert value('352') == 100
    assert value('0') == 100
    assert value('-6') == 100


def test_misc():
    assert value('') == 100
    assert value('!$$>?@<') == 100
    assert value(' ') == 100
