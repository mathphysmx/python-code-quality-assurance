"""Simple math operations used for example and tests.

Functions:
- add(a, b)
- multiply(a, b)
- divide(a, b)
"""

from __future__ import annotations


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return division `a / b`.

    Raises `ZeroDivisionError` when `b` is zero.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
