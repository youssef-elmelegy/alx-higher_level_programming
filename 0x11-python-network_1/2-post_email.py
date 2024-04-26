#!/usr/bin/python3
"""
    script that takes in a URL and an email,
    sends a POST request to the passed URL with the email as a parameter.
"""
import sys
import urllib.request as rq
from urllib import parse 

if __name__ == "__main__":
    email = {"email": sys.argv[2]}
    req = rq.Request(sys.argv[1], parse.urlencode(email).encode("ascii"))
    with rq.urlopen(req) as response:
        print(response.read().decode("utf-8", "replace"))
