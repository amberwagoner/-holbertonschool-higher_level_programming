#!/usr/bin/python3
""" Takes in URL, sends in request, displays value of variable """
import requests
import sys


if __name__ == '__main__':
    response = requests.get(argv[1])
    print(response.headers.get('X-Request-Id'))
