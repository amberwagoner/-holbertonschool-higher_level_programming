#!/usr/bin/python3
""" Defines the class MyList """


class MyList(list):
    """ Implements sorted printing """

    def print_sorted(self):
        """ Prints a list """
        print(sorted(self))
        