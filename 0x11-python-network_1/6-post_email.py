#!/usr/bin/python3
""" python script that manages email POSt"""
import requests
from sys import argv


if __name__ == '__main__':
    url, email = argv[1:]
    w = requests.Session()

    content = {'email': email}
    response = w.post(url, content=content)
    body = response.text
    print(body)
