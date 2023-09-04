#!/usr/bin/python3
""" Script that takes in a URL and displays the value of
the variable X-Request-Id in the response header"""
import requests
import sys


if __name__ == '__main__':
    the_value = requests.get(sys.argv[1])
    print(the_value.headers.get('X-Request-Id'))
