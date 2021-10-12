#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Sept 2021
# This program calculates the area and perimeter of a rectangle
#    with radius inputted from the user

import math


def main():
    # this function calculates the area and perimeter of a circle

    # input
    length = int(input("Enter length of rectangle (mm): "))
    width = int(input("Enter width of rectangle (mm): "))

    # process
    area = length * width
    perimeter = 2 * (length + width)

    # output
    print("")
    print("Area is {0} mm².".format(area))
    print("Perimeter is {0} mm.".format(perimeter))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
