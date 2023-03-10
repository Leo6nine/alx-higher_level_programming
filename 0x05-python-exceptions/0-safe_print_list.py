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
    count = 0
    if (x > 0):
        for i in range(x):
            try:
                print(f"{my_list[i]}", end="")
                count += 1
            except Exception:
                break
    print()
    return count
