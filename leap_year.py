#!/usr/bin/env python3

# Created By: Luke Di Bert
# Date: April 3, 2025

# adds random module
import random

# adds math module
import math


def main():

    # Gets the year as a variable from the user
    current_year = input("What is the year?: ")

    # Tries to convert the year to an integer then performs a series of calculations to determine wether or not it will be a leap year
    try:
        current_year = int(current_year)
        if current_year % 4 == 0:
            if current_year % 100 == 0:
                if current_year % 400 == 0:
                    print("It's a leap year!")
                else:
                    print("It's not a leap year")
            else:
                print("It's a leap year!")
        else:
            print("It's not a leap year")

    # If the given year is NOT able to be converted to an integer then it displays a message
    except:
        print(current_year, "is not an integer")

    # End message
    finally:
        print("Have a good day!")


if __name__ == "__main__":
    main()
