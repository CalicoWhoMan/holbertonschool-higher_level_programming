#!/usr/bin/python
"""github id displays"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    nic = requests.get('https://api.github.com/user',
                       auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    print(nic.json().get('id'))
