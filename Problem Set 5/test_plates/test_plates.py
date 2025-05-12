from plates import is_valid

def test_start_2_letters():
    assert is_valid("CS50") == True
    assert is_valid("A12345") == False

def test_length():
    assert is_valid("CS502025") == False
    assert is_valid("C") == False
    assert is_valid("CSDAN") == True

def test_endswith_numbers():
    assert is_valid("CS50D") == False
    assert is_valid("CS123") == True

def test_first_number_not_0():
    assert is_valid("CS0123") == False
    assert is_valid("DAN123") == True

def test_alphanumeric():
    assert is_valid("CS!@#") == False
    assert is_valid("DN123") == True
