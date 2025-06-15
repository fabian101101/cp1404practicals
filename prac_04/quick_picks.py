"""
CP1404/CP5632 Practical
Quick Pick Lottery Ticket Generator
"""

import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6


def main():
    """Generate user-specified number of quick pick lottery lines."""
    num_picks = int(input("How many quick picks? "))
    for _ in range(num_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in quick_pick))


def generate_quick_pick():
    """Generate a sorted list of 6 unique random numbers between 1 and 45."""
    numbers = []
    while len(numbers) < NUMBERS_PER_LINE:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:  # Ensure no duplicates
            numbers.append(number)
    return sorted(numbers)  # Return numbers in ascending order


main()
