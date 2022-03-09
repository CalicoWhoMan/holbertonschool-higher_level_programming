#!/usr/bin/python3
"""Takes URL, sends request to it, displays the value of X-Request-Id"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(response.__dict__['headers']['X-Request-Id'])
