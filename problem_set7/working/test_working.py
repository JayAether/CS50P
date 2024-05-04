from working import convert
import pytest


def test_convert_valid():
    assert convert('5 AM to 9 PM') == '05:00 to 21:00'
    assert convert('4:30 AM to 7:30 PM') == '04:30 to 19:30'
    assert convert('12 AM to 10 PM') == '00:00 to 22:00'
    assert convert('2 AM to 12 AM') == '02:00 to 00:00'
    assert convert('2 AM to 12 PM') == '02:00 to 12:00'


def test_convert_invalid():
    with pytest.raises(ValueError):
        convert('05:00 to 21:00')
    with pytest.raises(ValueError):
        convert('5 0')
    with pytest.raises(ValueError):
        convert('according to all laws of aviation')
    with pytest.raises(ValueError):
        convert('9AM to 5PM')
    with pytest.raises(ValueError):
        convert('13 AM to 5 PM')
    with pytest.raises(ValueError):
        convert('6:19 AM 4:20 PM')
    with pytest.raises(ValueError):
        convert('09:00 to 17:00')
    with pytest.raises(ValueError):
        convert(' to ')
    with pytest.raises(ValueError):
        convert('  2 AM to 12 PM f')
    with pytest.raises(ValueError):
        convert('')
    with pytest.raises(ValueError):
        convert(' ')
