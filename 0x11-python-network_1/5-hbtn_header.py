#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""
import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    w = requests.Session()

    response = w.get(url)
    body = response.text

    print(response.headers.get('X-Request-Id'))
