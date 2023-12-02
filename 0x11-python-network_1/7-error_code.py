#!/usr/bin/python3
"""displays the body of a requested URL
"""
import sys
import requests


if __name__ == "__main__":
    u = sys.argv[1]

    req = requests.get(u)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
