#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        func = fct(*args)
        return func
    except (TypeError, ValueError, IndexError, ZeroDivisionError):
        print("Exception: ".format(sys.exc_info()[1]), file=sys.stderr)
        return None
