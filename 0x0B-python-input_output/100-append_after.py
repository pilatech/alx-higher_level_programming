#!/usr/bin/python3
"""append_after Module"""


def append_after(filename="", search_string="", new_string=""):
    if filename:
        with open(filename, "a+", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                found = line.find(search_string)
                if (found != -1):
                    index = line.find('\n') + 1
                    f.seek(index)
                    f.write(new_string)

            

