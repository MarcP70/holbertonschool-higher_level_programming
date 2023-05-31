#!/usr/bin/python3
def uppercase(str):
    if (str):
        for char in str:
            if (ord(char) in range(97, 123)):
                print("{}".format(chr(ord(char)-32)), end="")
            else:
                print("{}".format(char), end="")
        print()
