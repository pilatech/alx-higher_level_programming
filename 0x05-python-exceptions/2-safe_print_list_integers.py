#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            item = my_list[i]
            if isinstance(my_list[i], int):
                print("{:d}".format(item), end="")
                count += 1
    except Exception as err:
        print(err)
    else:
        print("")
        return count
