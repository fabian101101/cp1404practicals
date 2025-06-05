"""
CP1404/CP5632 - Practical
Pseudocode for score menu program:
    get valid score
    display menu
    get choice and convert to uppercase
    while choice is not "Q"
        if choice is "G"
            get new valid score
        else if choice is "P"
            display score result
        else if choice is "S"
            display stars equal to score
        else
            display invalid choice message
        display menu
        get choice and convert to uppercase
    display farewell message
"""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Run a menu-driven program to manage scores."""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(get_score_result(score))
        elif choice == "S":
            print_stars(int(score))
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye!")


def get_valid_score():
    """Get a score between 0 and 100 inclusive."""
    while True:
        try:
            score = float(input("Enter score: "))
            if 0 <= score <= 100:
                return score
            print("Score must be between 0 and 100.")
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


def print_stars(num_stars):
    """Print stars equal to the given number."""
    print("*" * num_stars)


if __name__ == "__main__":
    main()
