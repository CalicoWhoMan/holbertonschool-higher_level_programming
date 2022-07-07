#!/usr/bin/python3
"""Take url, send req to url and display response"""
if __name__ == "__main__":
    from sys import argv
    import urllib.request
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except Exception as excep:
        print("Error code: {}".format(excep.code))
