#!/usr/bin/python3
"""Basic data fetching using urllib"""
if __name__ == "__main__":
    from urllib import request
    from urllib import error
    req = "https://alx-intranet.hbtn.io/status"
    try:
        resp = request.urlopen(req)
        print(dir(resp))
        print(resp.read().decode('utf-8'))
        print(resp.status)
    except error.HTTPError as e:
        print("Error code: {}".format(e.reason(0)))
