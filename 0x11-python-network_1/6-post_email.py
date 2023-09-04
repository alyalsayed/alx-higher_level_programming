#!/usr/bin/python3
"""Script that takes in a URL and an email
sends a POST request to the passed URL with the email
as a parameter and displays the body of the response"""
import requests
import sys


if __name__ == '__main__':
    the_value = {'email': sys.argv[2]}
    the_req = sys.argv[1]
    the_val = requests.post(the_req, the_value)
    print(the_val.text)
