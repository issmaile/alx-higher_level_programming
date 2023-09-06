#!/usr/bin/python3
"""Defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """Print a name

    Args:
        first_name (str): The 1st name to print
        last_name (str): The 2nd name to print

    Releases:
        TypeError: If first_name of last_name are not string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
