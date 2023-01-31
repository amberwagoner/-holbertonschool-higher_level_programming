#!/usr/bin/python3
""" Defines a subclass Square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Defines a square """

    def __init__(self, size):
        """ Initializes square """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ Returns area """
        return self.__size ** 2
