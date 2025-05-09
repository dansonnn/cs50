from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0

def test_start_h():
    assert value("hey") == 20
    assert value("HEY") == 20

def test_wrong():
    assert value("what's up?") == 100
    assert value("WHAT'S UP?") == 100
