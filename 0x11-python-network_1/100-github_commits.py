#!/usr/bin/python3
""" python script that takes my github cred and disp my id"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == '__main__':
    githRep, user = argv[1:]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(user, githRep)

    w = requests.Session()

    response = w.get(url)
    commits = response.json()[:10]
    for i in commits:
        print(i.get('sha'), end=': ')
        print(i.get('commit').get('author').get('name'))
