from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(20)
    assert jar.capacity == 20
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(4)
    assert jar.size == 9
    with pytest.raises(ValueError):
        jar.deposit(10)


def test_withdraw():
    jar = Jar(30) #capacity 30
    jar.deposit(20) #size 20
    jar.withdraw(5)
    assert jar.size == 15
    jar.withdraw(10)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.withdraw(9)


