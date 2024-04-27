#!/usr/bin/python3
"""Get github credentials"""
if __name__ == "__main__":
    import requests
    import sys
    url = "https://api.github.com/" + sys.argv[1]
    print(url)
    Auth = f"Bearer {sys.argv[2]}"
    r = requests.get(url, headers={"Authorization": Auth})
    if 'id' in r.json():
        print(r.json()['id'])
