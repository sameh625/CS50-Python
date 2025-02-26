from twttr import shorten

def test_with_vowels():
    assert shorten("sameh") == "smh"
    assert shorten("ali") == "l"
    assert shorten("aie") == ""


def test_without_vowels():
    assert shorten("kmpl") == "kmpl"
    assert shorten("pwbmvcx") == "pwbmvcx"
    assert shorten("TEST.") == "TST."

def test_capitalize():
    assert shorten("SAMEH") == "SMH"

def test_numbers():
    assert shorten("20.15") == "20.15"





