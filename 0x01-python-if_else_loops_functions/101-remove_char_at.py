#!/usr/bin/python3
def remove_char_at(str, n):
    return ''.join([c for i, c in enumerate(str) if i != n])
