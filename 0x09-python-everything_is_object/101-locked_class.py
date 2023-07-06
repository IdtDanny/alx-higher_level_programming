#!/usr/bin/python3
"""Defining a locked class in Python"""


class LockedClass:
    """
    Prevent user from instantianting any newly named LockedClass attributes
    for anything but attributes called 'first_name'.
    """
    __slots__ = ["first_name"]
