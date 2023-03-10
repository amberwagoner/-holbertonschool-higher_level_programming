#!/usr/bin/python3
""" Sends a post request to given url/email, displays decoded results """
from urllib.request import urlopen
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data_dict = {'email': email}
    utf8data = urlencode(data_dict).encode("utf-8")

    with urlopen(url, data=utf8data) as response:
        body = response.read()
        print(body.decode("utf-8"))
