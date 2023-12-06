#!/usr/bin/python3
"""reqs a given url and displays its X-Request-Id
"""
import sys
import requests


if __name__ == "__main__":
    u = sys.argv[1]
    r = requests.get(u)
    print(r.headers.get("X-Request-Id"))
