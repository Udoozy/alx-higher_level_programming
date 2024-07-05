#!/bin/bash
# Script that takes URL and sends a POST rqst to URL.
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
