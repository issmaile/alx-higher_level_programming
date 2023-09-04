#!/usr/bin/python3
"""
This module defines a function that adds two integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
    a (int): a
    b (int, optional): b

    Returns:
    int: Sum of a and b.

    Raises:
    TypeError: If a or b is not an int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")


    return int(a) + int(b)
