"""
CP1404/CP5632 Practical - Guitar class.
Estimated time: 30 minutes
Actual time: 25 minutes
"""


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance.

        name: str, name of the guitar
        year: int, year the guitar was made
        cost: float, cost of the guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar object."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar in years (current year - guitar's year)."""
        current_year = 2025  # Current year based on provided date
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old, False otherwise."""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Compare guitars by year for sorting (less than)."""
        return self.year < other.year
