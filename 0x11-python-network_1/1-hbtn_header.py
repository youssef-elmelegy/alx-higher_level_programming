#!/usr/bin/python3
"""
    Python script that takes in a URL, sends a request to the URL and
    displays the value of the X-Request-Id variable found in the response
"""
import sys
import urllib.request as rq


if __name__ == "__neme__":
    """you can't import this file"""
    req = rq.Request(sys.argv[1])
    with rq.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
