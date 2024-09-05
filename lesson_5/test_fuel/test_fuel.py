import pytest
from fuel import convert, gauge

def test_good_value():
    assert convert("2/4") == 50
    assert convert("3/4") == 75
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
    assert gauge(1) == "E"

def test_ValueError():
    with pytest.raises(ValueError):
        convert("4/2") #x > y
        convert("cat/dog") #not int
        convert("1/cat")
        convert("cat/2")

def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
        convert("100/0")
