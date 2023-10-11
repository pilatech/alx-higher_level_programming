#!/usr/bin/python3

for num in range(10):
    for num2 in range(num + 1, 10):
        if num == 0 and num2 == 1:
            print(f"{num}{num2}", end="")
            continue
        print(f", {num}{num2}", end="")
print("")
