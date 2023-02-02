#!/usr/bin/python3
""" Almost a Circle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes class """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Creates a new string """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """ Assigns value to size """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value

    def update(self, *args, **kwargs):
        """ Assigns an agrument to each attribute """
        if args:
            attributes = ["id", "size", "x", "y"]
            for ii in range(len(args)):
                setattr(self, attributes[ii], args[ii])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
