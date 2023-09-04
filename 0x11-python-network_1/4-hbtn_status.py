#!/usr/bin/python3
""" Script that fetches https://alx-intranet.hbtn.io/status """
import requests


if __name__ == '__main__':
    the_req = requests.get('https://alx-intranet.hbtn.io/status')
    the_text = the_req.text
    print('Body response:')
    print('\t- type: {}'.format(type(the_text)))
    print('\t- content: {}'.format(the_text))
