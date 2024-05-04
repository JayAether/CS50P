from twttr import shorten


def test_vowels_only():
    assert shorten("aauuiiooee") == ""
    assert shorten("eia") == ""
    assert shorten("e") == ""


def test_consonants_only():
    assert shorten("lbgsdb") == "lbgsdb"
    assert shorten("dsvvb") == "dsvvb"
    assert shorten("kll m pls") == "kll m pls"


def test_words():
    assert shorten("according to all laws of aviation") == "ccrdng t ll lws f vtn"
    assert (
        shorten("You can only restrain Me through words...")
        == "Y cn nly rstrn M thrgh wrds..."
    )
    assert shorten("I WILL RETURN!") == " WLL RTRN!"
    assert shorten("no?") == "n?"


def test_odd():
    assert shorten(" ") == " "
    assert shorten("a") == ""
    assert shorten("") == ""
    assert shorten("42") == "42"
    assert shorten("111111111111111111111111") == "111111111111111111111111"
    assert shorten(".!,?/") == ".!,?/"
