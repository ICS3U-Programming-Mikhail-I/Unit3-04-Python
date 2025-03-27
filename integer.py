#!/usr/bin/env python3
# Author: Mikhail Ibrahim
# Date: Mar 26, 2025
# Description: A program that checks if a number is positive, negative, or zero.

# Ask the user for an integer input
number = int(input("Enter an integer: "))

# Check if the number is positive, negative, or zero
if number > 0:
    print(f"{number} is a positive number.")  # Positive number message
elif number < 0:
    print(f"{number} is a negative number.")  # Negative number message
else:
    print(f"{number} is just zero!")  # Zero message
