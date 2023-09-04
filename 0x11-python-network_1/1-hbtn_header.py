#!/usr/bin/python3
""" Script that takes in a URL and displays the value
of the X-Request-Id variable found in the response header"""
import urllib.request
import sys


if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as res:
        html = res.info()
        print(html.get('X-Request-Id'))
