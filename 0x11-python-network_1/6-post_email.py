#!/usr/bin/python3
"""Send a post request carrying an email"""
if __name__ == "__main__":
    import requests
    import sys
    r = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(r.text)
