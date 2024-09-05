from plates import is_valid

def test_beggining_alphabetical():
    assert is_valid("25") == False
    assert is_valid("CS") == True

def test_number_of_character():
    assert is_valid("ESPAÑA50") == False
    assert is_valid("ESPAÑA") == True

def test_end_numbers():
    assert is_valid("CS50P2") == False
    assert is_valid("CSP50") == True

def test_zero():
    assert is_valid("CS05") == False
    assert is_valid("CSP50") == True

def test_no_special_characters():
    assert is_valid("PS.*") == False
    assert is_valid("WTF10") == True
