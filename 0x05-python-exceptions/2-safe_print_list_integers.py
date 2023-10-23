#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
             item = my_list[i]
        except Exception as err:
            print(err)
        else:
            if isinstance(my_list[i], int):
                print("{:d}".format(item), end="")
                count += 1
    print("")
    return count
