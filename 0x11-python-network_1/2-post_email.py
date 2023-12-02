#!/usr/bin/python3
"""A script that sends an email as param and di
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    u = sys.argv[1]
    val = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(val).encode("ascii")

    r = urllib.request.Request(u, data)
    with urllib.request.urlopen(r) as resp:
        print(resp.read().decode("utf-8"))
