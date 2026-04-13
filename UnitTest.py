"""
Unit test is used to check our code,
whether it is providing a desired output or not.

we can use pytest module for the same.

"""


def square(n):
    return n*n


def test_square():
    """
    assert : this asserts whether the output is same or not,
            if it is not then it throws assertion error.
    """
    assert square(1) == 1
    assert square(2) == 4
    assert square(5) == 25
    assert square(0) == 0
    assert square(-3) == 9


test_square()
