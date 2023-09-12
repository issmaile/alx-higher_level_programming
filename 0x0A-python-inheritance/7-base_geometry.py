#!/usr/bin/python3
"""asdasdasfdasfadfgsdfghsfgh Goe"""


class BaseGeometry:
    """Represent base geometry"""

    def area(self):
        """ASdfadfadf"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """asfadfgasdg

        Args:
        name (str): asdasd
        value (int): asadsf
        Raises:
        TypeError: asasf
        ValueError: asfaf
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
