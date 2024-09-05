from numb3rs import validate


def test_number_in_range():
    assert validate("255.255.255.255") == True
    assert validate("275.3.6.28") == False


def test_is_ip():
    assert validate("255.17.23.149") == True
    assert validate("cat") == False
