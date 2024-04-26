#!/usr/bin/python3
"""Basic data fetching using urllib"""
if __name__ == "__main__":
    from urllib import request
    with request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
        data = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data.decode('utf-8')))
