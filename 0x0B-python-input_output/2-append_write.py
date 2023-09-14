#!/usr/bin/python3
"""asfa"""


def append_write(filename="", text=""):
    """asfaF
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
