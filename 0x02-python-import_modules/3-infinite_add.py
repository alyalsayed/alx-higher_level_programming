#!/usr/bin/env python3
import sys

def main():
    args = sys.argv[1:]
    total = sum(map(int, args))
    print(total)

if __name__ == "__main__":
    main()
