#!/usr/bin/python3
""" Defines a class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class """

    def __init__(self, width, height):
        """ Initializes new rectangle """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Returns area """
        return self.__width * self.__height

    def __str__(self):
        """ Creates a new string object """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
