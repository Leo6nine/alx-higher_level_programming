#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
        
    op = argv[2]
    sign = {"+": add, "-": sub, "*": mul, "/": div}
    if op not in sign:
        print("Unknown operater. Available poerators: +, -, *, and /")
        exit (1)
    a = int(argv[1])
    b = int(argv[3])
    print("{:d} {:s} {:d} = {:d}".format(a, op, b, sign[op](a, b)))
