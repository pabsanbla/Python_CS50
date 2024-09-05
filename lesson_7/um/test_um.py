from um import count

def test_words_with_um():
    assert count("instrumentation") == 0
    assert count("Um, what a yuumi ice-cream") == 1
    assert count("Um, do you know about this, um; documentary about monuments?") == 2


def test_punctuation():
    assert count("um, humidification; um.") == 2
    assert count("Um? um! circumsition") == 2
    assert count("um; humidity") == 1


def test_indiference():
    assert count("UM, um, Um, uM") == 4


