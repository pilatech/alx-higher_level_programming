#!/usr/bin/python3
"""Mini json search api"""
if __name__ == "__main__":
    import requests
    import sys
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = ""
    url = "http://0.0.0.0:5000/" + arg
    r = requests.post(url, json={"q": arg})
    print(r.text)
    try:
        data = r.json()
        if not bool(data):
            print("No result")
        else:
            print(f"[{data['id']}] {data['name']}")
    except Exception:
        print("Not Valid JSON")
