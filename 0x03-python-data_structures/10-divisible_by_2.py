#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return []
    return [a % 2 == 0 for a in my_list]
