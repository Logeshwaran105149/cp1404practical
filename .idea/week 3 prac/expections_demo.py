"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   A ValueError will occur when the arguments passed to a function or method are of the correct type but are inappropriate
   values,or when the arguments are of the wrong type.

2. When will a ZeroDivisionError occur?
   A ZeroDivisionError occurs when we try to divide a number by zero. For example, if we have the expression x = 1 / 0,
   it will raise a ZeroDivisionError because we cannot divide a number by zero.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   we can avoid the possibility of a ZeroDivisionError by adding a check to make sure that the denominator is not zero
   before performing the division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("denominator cant divided by zero ")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
