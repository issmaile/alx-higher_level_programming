#!/usr/bin/python3
"""Defines an obj attr lookup func"""


def loopup(obj):
    """Ret a list of an obj's attrs"""
    return (dir(obj))
