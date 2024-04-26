#!/usr/bin/python3
"""Send post request with an email"""
if __name__ == "__main__":
    from urllib import request
    import sys
    payload = {"email": sys.argv[2]}
    req = request.Request(sys.argv[1], payload)
    with request.urlopen(req) as resp:
        print(resp.read().decode('utf-8'))
