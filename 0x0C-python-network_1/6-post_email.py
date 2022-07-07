#!/usr/bin/python3
"""POST an email using URL and email"""
if __name__ == "__main__":
    import requests
    import sys
    email = sys.argv[2]
    value = {"email": email}
    r = requests.post(sys.argv[1], value)
    print(r.text)
