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
    
    x = argv[1]
    y = argv[3]
    a = int(x)
    b = int(y)
    
    if op == '+':
        tmp = add(a, b)
        print("{} + {} = {}".format(x, y, tmp))
    elif op == '-':
        tmp = sub(a, b)
        print("{} - {} = {}".format(x, y, tmp))
    elif op == '*':
        tmp = mul(a, b)
        print("{} * {} = {}".format(x, y, tmp))
    elif op == '/':
        tmp = div(a, b)
        print("{} / {} = {}".format(x, y, tmp))
