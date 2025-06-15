"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    - A `ValueError` will occur when the input for either the numerator or the denominator is
     not a valid integer. Example include; asd, 23@, #56, etc.

2. When will a ZeroDivisionError occur?
    - A `ZeroDivisionError` will occur when the denominator is zero.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    - Yes, I can do this by checking if the denominator is zero before performing the division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # Check if the denominator is zero and prompt the user to enter a non-zero denominator
    while denominator == 0:
        print("Denominator cannot be zero!")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
