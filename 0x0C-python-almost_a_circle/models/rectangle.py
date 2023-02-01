#!/usr/bin/python3
""" Almost a Circle """
from models.base import Base


class Rectangle(Base):
    """ Inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes class """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: Assigns value to width"""
        return self.__width

    @property
    def height(self):
        """int: Assigns value to height"""
        return self.__height

    @property
    def x(self):
        """int: Assigns value to x"""
        return self.__x

    @property
    def y(self):
        """int: Assigns value to y"""
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns area of Rectangle """
        return self.__width * self.__height

    def display(self):
        """ Prints Rectangle to stdout """
        for i in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print('#', end="")
            print()
