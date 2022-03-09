#!/usr/bin/python3
"""Takes URL, sends request to it, displays the value of X-Request-Id"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    email_values = {'email' : email}
    data = urllib.parse.urlencode(email_values)
    data = data.encode(encoding='utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read())
