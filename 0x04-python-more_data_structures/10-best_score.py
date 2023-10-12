#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary or len(a_dictionary) == 0:
        return None
    largest = a_dictionary[list(a_dictionary)[0]]
    highest = list(a_dictionary)[0]
    for key, val in a_dictionary.items():
        if val > largest:
            highest = key
    return highest
