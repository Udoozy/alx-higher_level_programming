#!/bin/bash
# This takes url ans displays all HTTP methods
curl -sI "$1" | grep "Allow:" | cut -d " " -f2-
