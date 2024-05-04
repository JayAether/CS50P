from um import count


def test_count():
    assert count('um') == 1
    assert count('um um um') == 3
    assert count('UM, Um?') == 2
    assert count('umumumum uuummm') == 0
    assert count('whatum sayum') == 0

