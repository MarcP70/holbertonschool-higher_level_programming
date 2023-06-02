#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]
    argc = len(argv)

    if argc > 0:
        result = sum(int(arg) for arg in argv)
        print("{}".format(result))
