#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    counter = len(argv) - 1
    if counter == 0:
        print("{} arguments:".format(counter))
    elif counter == 1:
        print("{} argument:".format(counter))
        print("{}: ".format(counter) + argv[1])
    else:
        print("{} arguments:".format(counter))
    for i in range(1, len(argv[i])):
        print('{}: {}'.format(i, argv[i]))
