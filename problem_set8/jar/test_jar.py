from jar import Jar
import pytest


def test_init():
    Jar()


def test_str():
    jar = Jar()

    assert str(jar) == ''
    jar.deposit(10)
    assert str(jar) == '🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪'
    jar.withdraw(5)
    assert str(jar) == '🍪🍪🍪🍪🍪'


def test_deposit():
    jar = Jar()

    jar.deposit(2)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.deposit(245)


def test_withdraw():
    jar = Jar()

    jar.deposit(5)
    assert jar.size == 5
    jar.withdraw(2)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(5)

