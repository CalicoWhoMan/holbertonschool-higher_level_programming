#!/usr/bin/python3
"""Script that fetches this link -> https://intranet.hbtn.io/status"""

import urllib.request

x = urllib.request.urlopen('https://intranet.hbtn.io/status')
print(x.read())
# with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
