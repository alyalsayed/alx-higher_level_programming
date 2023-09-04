#!/usr/bin/python3
"""Script that takes in a URL and
displays the body of the response """
import requests
import sys


if __name__ == '__main__':
    the_req = requests.get(sys.argv[1])
    if the_req.status_code >= 400:
        print("Error code: {}".format(the_req.status_code))
    else:
        print(the_req.text)
