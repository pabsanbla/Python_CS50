from twttr import shorten

test_words = ["Twitter", "SPAIN", "Harry Potter", "EE.UU", "AeOluS"]

def test_upper():
    assert shorten(test_words[1]) == "SPN"
    assert shorten(test_words[3]) == "."

def test_lower():
    assert shorten(test_words[0]) == "Twttr"
    assert shorten(test_words[2]) == "Hrry Pttr"



