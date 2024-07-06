#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status"""
import requests


if __name__ == '__main__':
    w = requests.Session()

    response = w.get('https://intranet.hbtn.io/status')
    body = response.text

    print('Body response:')
    print('\t- type: {}'.format(type(body)))
    print('\t- content: {}'.format(body))
