#!/usr/bin/env python3
def islower(c):
    for i in range(ord('a'), ord('z') + 1):
        if c == i:
            return True
        else:
            return False
