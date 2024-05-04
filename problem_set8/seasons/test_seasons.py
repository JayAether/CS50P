from seasons import date_validity, get_date, become_minute_words


def date_validity():
    assert date_validity([123, 2, 7])
    assert not date_validity([-123, -2, -7])
    assert not date_validity([12423, 2, 7])
    assert not date_validity([123, 2, 75])
    assert not date_validity([123, 422, 7])


def test_get_date():
    assert get_date('123-2-7') == [123, 2, 7]
    assert get_date('1-12-27') == [1, 12, 27]


def test_become_minute_words():
    assert become_minute_words(1) == 'One thousand, four hundred forty minutes'
    assert become_minute_words(366) == 'Five hundred twenty-seven thousand forty minutes'

