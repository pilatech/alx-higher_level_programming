#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    import calculator_1 as cal
    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if argv[2] == "+":
        print("{} + {} = {}".format(a, b, cal.add(a, b)))
    elif argv[2] == "-":
        print("{} - {} = {}".format(a, b, cal.sub(a, b)))
    elif argv[2] == "*":
        print("{} * {} = {}".format(a, b, cal.mul(a, b)))
    elif argv[2] == "/":
        print("{} / {} = {}".format(a, b, cal.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
