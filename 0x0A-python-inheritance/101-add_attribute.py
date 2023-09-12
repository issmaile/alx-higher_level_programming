#!/usr/bin/python3
"""asdasdasda"""


def add_attribute(obj, att, value):
    """asdasdasd

    Args:
        obj (any): asdasd
        att (str): asdasd
        value (any): asdasd
    Raises:
        TypeError: if attr cant be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
