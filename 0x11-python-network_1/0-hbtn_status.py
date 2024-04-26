#!/usr/bin/python3
"""fetch url"""

import urllib.request as rq


if __name__ == __main__:
    """ Python script that fetches https://alx-intranet.hbtn.io/status """


    req = rq.Request("https://alx-intranet.hbtn.io/status")
    with rq.urlopen(req) as response:
        data = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data.decode("utf-8")))
