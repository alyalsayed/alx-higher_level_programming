#!/usr/bin/env python3
import sys

def main():
    args = sys.argv[1:]
    num_args = len(args)

    # Print number of arguments
    print("{} argument{}:".format(num_args, "" if num_args == 1 else "s"))

    # Print list of arguments
    for i, arg in enumerate(args):
        print("{}: {}".format(i+1, arg))

if __name__ == "__main__":
    main()
