#!/usr/bin/python3
""" define class Square"""


class Square:
    """class with private size field"""
    def __init__(self, size=0):
        if (type(size) != int):
            raise TypeError('size must be an integer')
        if (size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size
