#!/usr/bin/python3


def uniq_add(my_list=[]):
    unique = 0
    for x in set(my_list):
        unique += x
    return unique
