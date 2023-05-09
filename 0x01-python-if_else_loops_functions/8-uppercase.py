#!/usr/bin/env python3
def uppercase(s):
    result = ""
    for c in s:
        if ord(c) >= 97 and ord(c) <= 122:
            result += chr(ord(c) - 32)
        else:
            result += c
    print(result + "\n", end="")
