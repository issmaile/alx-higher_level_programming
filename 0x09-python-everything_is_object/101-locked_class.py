#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from instantiation new attributes in LockedClass
    other than the one called 'first_name'
    """

    __slots__ = ["first_name"]