#!/usr/bin/python3
"""Module for adding all arguments to Python list and saving to file"""
import sys
import json
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

f_ = 'add_item.json'

if os.path.isfile(f_):
    data = load_from_json_file(f_)
    obj = list(data) + sys.argv[1:]
else:
    with open(f_, "w", encoding="utf-8"):
        pass
    obj = sys.argv[1:]

save_to_json_file(obj, f_)
data = load_from_json_file(f_)
