#!/usr/bin/python3
"""Script that fetches https://intranet.hbtn.io/status using requests"""

import requests


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    req = requests.get(url)
    print("Body responses:")
    print("  - type: {}".format(type(req.text)))
    print("  _ content: {}".format(req.text))
