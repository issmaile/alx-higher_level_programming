#!/usr/bin/python3
"""Defines a func that prints a square of given size"""


def print_square(size):
    """
    Print a square with # character of given size.

    Args:
        size (int): Square size (height or width)

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        [print("#", end="") for y in range(size)]
        print("")
