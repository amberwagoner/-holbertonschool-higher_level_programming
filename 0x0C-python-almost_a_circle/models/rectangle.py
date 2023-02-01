#!/usr/bin/python3
""" Almost a Circle """
from models.base import Base


class Rectangle(base):
    """ Inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes class """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
