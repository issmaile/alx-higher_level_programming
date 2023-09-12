#!/usr/bin/python3
"""asdasdasd"""


class MyInt(int):
    """asdasdasd"""

    def __eq__(self, value):
        """Override == with !="""
        return self.real != value

    def __ne__(self, value):
        """Overrd != with =="""
        return self.real == value
