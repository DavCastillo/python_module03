#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    argv = sys.argv
    argc = len(sys.argv)
    print("Program name:", argv[0])
    if (argc == 1):
        print("No arguments provided!")
    else:
        print("Arguments received:", (argc - 1))
        idx = 1
        while (idx < argc):
            print("Argument ", idx, ": ", argv[idx], sep='')
            idx += 1
    print("Total arguments:", argc)
