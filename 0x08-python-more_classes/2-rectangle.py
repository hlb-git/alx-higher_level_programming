#!/usr/bin/python3
"""define a rectangle"""


class Rectangle:
    """width and height attributes"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets value"""

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """gets height"""

        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """return area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """return perimeter of rectangle"""
        return (self.width * 2) + (self.height * 2)
