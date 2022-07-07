#!/usr/bin/python3
"""takes URL, sends req to URL, displays resp as val of var"""
if __name__ == "__main__":
    import requests
    import sys
    req = requests.get(sys.argv[1])
    print(req.headers.get("X-Request-Id"))
