#!/usr/bin/python3
"""Module for adding all arguments to Python list and saving to file"""
import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

obj = sys.argv[1:]
save_to_json_file(obj, 'add_item.json')
obj = load_from_json_file('add_item.json')
print(obj)
