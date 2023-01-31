#!/usr/bin/python3
""" Function to create a class """


class BaseGeometry:
    """ Creates a class """

    def area(self):
        """ Defines area - not yet implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
