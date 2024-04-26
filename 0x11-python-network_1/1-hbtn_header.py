#!/usr/bin/python3
"""Get value of a header"""
if __name__ == "__main__":
    from urllib import request
    import sys
    with request.urlopen(sys.argv[1]) as resp:
        header = resp.getheader('X-Request-Id')
        print(header)
