from bank import value

def test_hello():
    assert value("Hello") == 0
    assert value("hello") == 0

def test_h_start():
    assert value("hi") == 20
    assert value("How are you?") == 20

def test_bad_greeting():
    assert value("What´s up") == 100
    assert value("what a beautiful day") == 100
