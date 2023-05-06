#!/usr/bin/bash/python3

import doctest

def add(a,b):
    """
    Adds two numbers and return the result

    >>> add(2,3)
    5
    >>> add(6,8)
    14
    >>> add(1,2)
    3
    """
    return a+b

if __name__ == "__main__":
    doctest.testmod(add)
