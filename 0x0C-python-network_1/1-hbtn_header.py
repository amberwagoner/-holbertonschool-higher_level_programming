#!/usr/bin/python3
""" Displays the X-Request-Id variable """
import sys
from sys import argv
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        print(response.headers["X-Request-Id"])
