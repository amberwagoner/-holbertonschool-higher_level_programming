#!/usr/bin/python3
""" Takes in a URL and email address and sends POST response """
import requests
import sys


if __name__ == "__main__":
    print(requests.post(sys.argv[1], data={'email': sys.argv[2]}).text)
