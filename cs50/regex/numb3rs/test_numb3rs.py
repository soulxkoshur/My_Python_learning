from numb3rs import validate
import pytest


def test_format():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.4") == True


def test_range():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("256.0.0.0") == False
    assert validate("127.300.1.2") == False 
    assert validate("127.1.300.2") == False  
    assert validate("127.1.2.300") == False
    

def test_non_numeric():
    assert validate("cat") == False
    assert validate("1.2.3.cat") == False
    assert validate("abc.def.ghi.jkl") == False


def test_invalid_octets():
    assert validate("1st.2nd.3rd.4th") == False
    assert validate("255.255.255") == False 
    assert validate("255.255.255.255.255") == False
