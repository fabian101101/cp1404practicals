"""
CP1404/CP5632 - Practical
Random numbers
"""

import random

# Line 1:
print(random.randint(5, 20))
# The smallest number I could have seen is 5, and the largest number is 20.

# Line 2:
print(random.randrange(3, 10, 2))
# The smallest number I could have seen is 3, and the largest number is 9.
# This line could not have produced a 4 because the step is 2 (possible values: 3, 5, 7, 9).

# Line 3:
print(random.uniform(2.5, 5.5))
# The smallest number I could have seen is 2.5, and the largest number is 5.5.

# Code to produce a random number between 1 and 100 inclusive
print(random.randint(1, 100))