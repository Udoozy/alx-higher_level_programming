#!/usr/bin/python3

"""script that takes a url send a request to url"""
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as res:
        body = res.read()
        print(res.headers['X-Request-Id'])
