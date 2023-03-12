#!/usr/bin/python3
""" Takes in URL, sends in request, displays value of variable """
import requests
from sys import argv


if __name__ == '__main__':
    print(requests.get(sys.argv[1]).headers.get('X-Request-Id'))
