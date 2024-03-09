#!/usr/bin/python3
"""Module for adding all arguments to Python list and saving to file"""
import sys
import json
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


f_ = 'add_item.json'

with open(f_, "a", encoding="utf-8"):
    pass
obj = load_from_json_file(f_) or []
obj = obj + sys.argv[1:]
save_to_json_file(obj, f_)
with open(f_, 'r', encoding="utf-8") as f:
    data = f.read()
    print(data)
