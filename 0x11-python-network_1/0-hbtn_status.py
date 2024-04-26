#!/usr/bin/python3
"""Basic data fetching using urllib"""
if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
        data = resp.read()
        print("Body response:")
        print(" - type: {}".format(type(data)))
        print(" - content: {}".format(data))
        print(" - utf8 content: {}".format(data.decode('utf-8')))
