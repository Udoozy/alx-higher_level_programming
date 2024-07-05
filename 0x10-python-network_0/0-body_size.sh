#!/bin/bash
# It takes in a URL send a request and displays result
curl -s "$1" | wc -c
