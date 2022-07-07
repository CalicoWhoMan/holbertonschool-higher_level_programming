#!/usr/bin/python3
"""Takes URL and email; sends POSTS req to URL  with email as param"""
if __name__ == "__main__":
    import sys
    import urllib
    from sys import argv
    from urllib import request, parse
    url = argv[1]
    value = {"email": argv[2]}
    data = parse.urlencode(value)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
