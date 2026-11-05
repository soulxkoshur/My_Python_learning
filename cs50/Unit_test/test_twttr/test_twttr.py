from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("how are you") == "hw r y"
    assert shorten("Hello123") == "Hll123"
    assert shorten("how are you?") == "hw r y?"
    assert shorten("HOW ARE YOU?") == "HW R Y?"


