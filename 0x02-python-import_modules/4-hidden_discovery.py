#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hidden
    nodunder = [el for el in dir(hidden) if el[0] != "_" and el[1] != "_"]
    for element in nodunder:
        print(element)
