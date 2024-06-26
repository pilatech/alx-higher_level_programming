#!/usr/bin/python3
"""Fetch data using requests and print specific header"""
if __name__ == "__main__":
    import requests
    import sys
    r = requests.get(sys.argv[1])
    if 'X-Request-Id' in r.headers.keys():
        print(r.headers['X-Request-Id'])
