#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("0 argument.")
    elif len(argv) == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(argv) - 1))
    if len(argv) != 1:
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
