#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    '''
    Print x elememts of a list.

    Args:
        @my_list: list of elements to print.
        x: The number of elements to print from my_list.

    Returns:
        The number of elements printed.
    '''
    num = 0
    while num < 0:
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            break
        num += 1
        print("")
        return num
