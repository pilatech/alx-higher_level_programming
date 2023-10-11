#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if (ord(str[i]) >= 97) and (ord(str[i]) <= 122):
            code = ord(str[i]) - 32
        else:
            code = ord(str[i])
        print("{}".format(chr(code)), end="")
    print("")
