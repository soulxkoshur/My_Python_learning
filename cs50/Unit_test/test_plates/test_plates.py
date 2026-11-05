from plates import is_valid

def main():
    test_is_valid()
    test_length_is_valid()
    test_first_is_valid()
    test_no_letters_after_numbers_is_valid()
    test_onlychar()
    test_start_letters()
    test_start_with_two_letters()
    test_only_alphanumeric()

def test_length_is_valid():
    assert is_valid("") == False
    assert is_valid("A") == False
    assert is_valid("AB") == True
    assert is_valid("ABC") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("ABCDEFG") == False

def test_first_is_valid():
    assert is_valid("A") == False
    assert is_valid("AB") == True
    assert is_valid("CS50") == True

def test_no_letters_after_numbers_is_valid():
    assert is_valid("CS50P") == False
    assert is_valid("CS05") == False

def test_onlychar():
    assert is_valid("ABC") == True
    assert is_valid("XYZ") == True

def test_start_letters():
    assert is_valid("AB") == True
    assert is_valid("CS50") == True

def test_start_with_two_letters():
    assert is_valid("1A") == False
    assert is_valid("A1") == False

def test_only_alphanumeric():
    assert is_valid("AB!?") == False
    assert is_valid("AB 12") == False
