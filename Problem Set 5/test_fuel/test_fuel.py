import fuel
import pytest

def test_empty():
    assert fuel.convert("0/1") == 0
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(1) == "E"

def test_full():
    assert fuel.convert("4/4") == 100
    assert fuel.gauge(100) == "F"
    assert fuel.gauge(99) == "F"

def test_more_than_100():
    with pytest.raises(ValueError):
        fuel.convert("5/4")

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("1/0")

def test_normal():
    assert fuel.convert("2/4") == 50
    assert fuel.gauge(50) == "50%"
