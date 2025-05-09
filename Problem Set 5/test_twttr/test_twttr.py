from twttr import shorten

def test_sentence():
    assert shorten("I am Danson") == " m Dnsn"

def test_uppercase():
    assert shorten("ABC EIF YOU") == "BC F Y"

def test_special_characters():
    assert shorten("This is CS50?!") == "Ths s CS50?!"
