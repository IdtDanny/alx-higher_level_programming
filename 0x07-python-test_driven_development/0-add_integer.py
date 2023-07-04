#!/usr/bin/python3
"""defining integer addition function."""


def add_integer(a, b=98):
    """"Return the sum of two integer passed through add_integer.

    floats are typcasted to int before addition performed.

    raises:
        TypeError: if either a or b is non-integer or non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
