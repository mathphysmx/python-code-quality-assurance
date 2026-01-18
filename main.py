"""Small demo runner for `mypkg`.

Run this file to see example usage of the package functions.
"""

from mypkg import add, divide, multiply


def demo() -> None:
    a, b = 8, 2
    print("demo: add", a, "+", b, "=", add(a, b))
    print("demo: multiply", a, "*", b, "=", multiply(a, b))
    print("demo: divide", a, "/", b, "=", divide(a, b))


if __name__ == "__main__":
    demo()
