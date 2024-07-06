#!/usr/bin/python3
""" Scrpt that takes url and email and send a post"""
from urllib import request, parse
import sys


if __name__ == '__main__':
    url, email = sys.argv[1:]
    body = {'email': email}
    content = parse.urlencode(body)
    content = content.encode('ascii')
    infom = request.Request(url, content)

    with request.urlopen(infom) as response:
        html = response.read()
        print(html.decode('utf-8'))
