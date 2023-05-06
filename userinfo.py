#!/usr/bin/bash
import doctest

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
        print("\n")

display_info(name="John", age=30, city="maryland")
display_info(name="Doe", age=28, city="texas")
display_info(name="Jane", age=20, city="toronto")

if __name__ == "__main__":
    doctest.testmod()

