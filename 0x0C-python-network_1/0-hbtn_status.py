#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status """
import urllib.request


url = 'https://intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body = response.read()
    content = body.decode('utf-8')

print("Body response:")
print("    - type: {}".format(type(body)))
print("    - content: {}".format(body))
print("    - utf8 content: {}".format(content))
