"""
General utility functions
"""
from __future__ import absolute_import


def number_format(number):
    """
    Number format utility. We include this so we can
    potentially alter the way / precision of displayed
    numbers in a central place.
    :param number:
    :return: String representation of the number
    """
    return "{num}".format(num=number)
