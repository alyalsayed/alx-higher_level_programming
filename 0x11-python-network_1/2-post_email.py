#!/usr/bin/python3
""" Script that takes in a URL and an email
sends a POST request to the passed URL with the email
as a parameter and displays the body of the response"""
import urllib.request
import urllib.parse
import sys


if __name__ == '__main__':
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    with urllib.request.urlopen(sys.argv[1], data) as res:
        html = res.read()
        print(html.decode('utf-8'))
