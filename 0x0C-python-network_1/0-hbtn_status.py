#!/usr/bin/python3
import urllib.request
"""Py script to fetch a website"""
with urllib.request.urlopen('https://intranet.hbtn.io/status') as request:
html = request.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf-8')))
