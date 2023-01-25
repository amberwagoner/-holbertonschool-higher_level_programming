#!/usr/bin/python3
""" rectangle """


class Rectangle:
    """ defines a rectangle """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ gets width """
        return self.__width

    @property
    def height(self):
        """ gets height """
        return self.__height

    @width.setter
    def width(self, value):
        """ sets width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if (0 > value):
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ sets height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if (0 > value):
            raise ValueError("height must be >= 0")
        self.__height = value
