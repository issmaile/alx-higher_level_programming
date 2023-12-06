#!/usr/bin/python3
"""displays body of response of a requested URL
"""
import sys
from urllib import request, error

if __name__ == "__main__":

    try:
        with request.urlopen(sys.argv[1]) as resp:
            print(resp.read().decode('UTF-8'))
    except error.HTTPError as err:
        print('Error code:', err.code)
