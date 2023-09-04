#!/usr/bin/python3
"""  Script that takes Github username and password
and uses github api to display your id"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == '__main__':
    the_url = "https://api.github.com/user"
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    the_req = requests.get(the_url, auth=auth)
    print(the_req.json().get('id'))
