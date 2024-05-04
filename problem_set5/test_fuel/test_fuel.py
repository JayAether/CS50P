from fuel import gauge, convert
import pytest


def test_convert():
    assert convert('10/10') == 100
    assert convert('0/10') == 0
    assert convert('4/10') == 40


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')


def test_value_error():
    with pytest.raises(ValueError):
        convert('cat/dog')


def test_gauge():
    assert gauge(100) == 'F'
    assert gauge(99) == 'F'
    assert gauge(98) == '98%'
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(2) == '2%'

