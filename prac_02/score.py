"""
CP1404/CP5632 - Practical
Pseudocode for score status program:
    get score
    while score input is invalid
        display error message
        get score
    if score < 0 or score > 100
        result is "Invalid score"
    else if score >= 90
        result is "Excellent"
    else if score >= 50
        result is "Passable"
    else
        result is "Bad"
    display result
    generate random score
    determine result for random score
    display random score and result
"""

import random


def main():
    """Get a user's score, display its result, and show a random score's result."""
    score = get_valid_score()
    result = get_score_result(score)
    print(result)
    random_score = get_random_score()
    print(f"Random score: {random_score}")
    random_result = get_score_result(random_score)
    print(random_result)


def get_valid_score():
    """Get a valid score from the user."""
    while True:
        try:
            score = float(input("Enter your score: "))
            return score
        except ValueError:
            print("Please enter a valid number.")


def get_score_result(score):
    """Return the result string for a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def get_random_score():
    """Generate a random score between 0 and 100."""
    return random.randint(0, 100)


main()
