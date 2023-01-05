#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    x = argv[1]
    y = argv[3]
    a = int(x)
    b = int(y)
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if argv[2] not in ["+", "-", "*", "/"]:
            print("Unknown operater. Available poerators: +, -, *, and /")
            exit (1)
        else:
            if argv[2] == '+':
                tmp = add(a, b)
                print("{} + {} = {}".format(x, y, tmp))
            elif argv[2] == '-':
                tmp = sub(a, b)
                print("{} - {} = {}".format(x, y, tmp))
            elif argv[2] == '*':
                tmp = mul(a, b)
                print("{} * {} = {}".format(x, y, tmp))
            elif argv[2] == '/':
                tmp = div(a, b)
                print("{} / {} = {}".format(x, y, tmp))
