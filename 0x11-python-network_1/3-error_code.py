#!/usr/bin/python3
"""Script that takes in a URL and
displays the body of the response """
import urllib.request
import urllib.error
import sys


if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        print('Error code: {}'.format(err.code))
