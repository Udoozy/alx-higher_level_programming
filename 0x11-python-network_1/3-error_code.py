#!/usr/bin/python3
""" Python that manages urllib.error.HTTPError"""
from urllib import error, request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with request.urlopen(url) as res:
            body = res.read()
            print(body.decode('utf-8'))
    except error.HTTPError as err:
        print('Error code: {}'.format(err.code))
