import pytest

from mypkg import add, divide, multiply


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(2.5, 2) == 5.0


def test_divide():
    assert divide(10, 2) == 5
    assert pytest.approx(divide(1, 3), 1e-9) == 1 / 3


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
