#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    total = 0

    if argc == 0:
        print("0")
    elif argc > 1:
        for i in range(1, len(sys.argv)):
            total += int(sys.argv[i])
        print(total)
