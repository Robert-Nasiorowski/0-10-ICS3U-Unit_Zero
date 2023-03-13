#!/usr/bin/env python3

"""
Created by Robert Nasiorowski 
Created on 2023-03-13
This program adds two numbers together
"""


def main() -> None:
    print("This program adds 0.1 and 0.2 together.")

    # process
    answer = 0.1 + 0.2

    # output
    print("")
    print("The answer is {:.2f}.".format(answer))

    print("\nDone.\n")


if __name__ == "__main__":
    main()
