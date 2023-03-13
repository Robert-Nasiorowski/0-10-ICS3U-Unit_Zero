#!/usr/bin/env python3

"""
Created by Robert Nasiorowski 
Created on 2023-03-13
This program adds two numbers together
"""

def main() -> None:
    # This function adds two numbers together

    # input
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))

    # process
    answer = first_number + second_number

    # output
    print("")
    print("The answer is {answer:.10f}.".format(answer))

    print("\nDone.\n")

if __name__ == "__main__":
    main()
