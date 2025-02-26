from bank import value

def test_0():
    assert value("hello") == 0
    assert value("HeLlo") == 0
    assert value("Hello, Newman") == 0

def test_20():
    assert value("How you doing?") == 20
    assert value("Hi, ali") == 20

def test_100():
    assert value("What's happening?") == 100
