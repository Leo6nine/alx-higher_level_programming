#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    i = 0
    for j in range(1, len(argv)):
        i += int(argv[j])
    print('{}'.format(i))
