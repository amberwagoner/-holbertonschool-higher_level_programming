#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status """
import urllib.request


def fetch_status_page(url):
    """ Fetches that URL! """
    with urllib.request.urlopen(url) as response:
        body = response.read()
        content = body.decode('utf-8')
    return {
        'type': type(body),
        'content': body,
        'utf8_content': content
    }

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    response_info = fetch_status_page(url)
    print("Body response:")
    print("    - type: {}".format(response_info['type']))
    print("    - content: {}".format(response_info['content']))
    print("    - utf8 content: {}".format(response_info['utf8_content']))
