#!/usr/bin/python3
"""Script that fetches this link -> https://intranet.hbtn.io/status"""

import urllib.request

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        print(response.read())
