#!/usr/bin/python3
"""
    script that takes in a URL,
    sends a request to the URL and displays the body of the response
"""
import sys
import urllib.request as rq
from urllib.error import HTTPError

if __name__ == "__main__":
    req = req.Request(sys.argv[1])
    try:
        with req.urlopen(req) as response:
            print(response.read().decode("ascii"))
    except HTTPError as hte:
        print(f"Error code: {hte.code}")
