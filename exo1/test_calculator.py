from calculator import add, divide, is_even
import pytest


def test_add():
    assert add(1,5) == 6

def test_divide_success():
    assert divide(8,2) == 4

def test_divide_failure():
    with pytest.raises(ValueError):
        divide(4,0)