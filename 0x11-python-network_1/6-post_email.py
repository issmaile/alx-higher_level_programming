#!/usr/bin/python3
"""displays X-Request-Id of a requst of a given URL
"""
import sys
import urllib.request

if __name__ == "__main__":
    u = sys.argv[1]
    req = urllib.request.Request(u)
    with urllib.request.urlopen(req) as res:
        print(dict(res.headers).get("X-Request-Id"))
