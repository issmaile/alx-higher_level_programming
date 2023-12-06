#!/usr/bin/python3
"""a script that take in an URL
- and proces some stuff
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    r = urllib.request.Request(url)
    with urllib.request.urlopen(r) as data:
        print(dict(data.headers).get("X-Request-Id"))
