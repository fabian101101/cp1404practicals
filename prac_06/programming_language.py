"""
CP1404/CP5632 Practical - ProgrammingLanguage class.
Estimated time: 30 minutes
Actual time: 35 minutes
"""


class ProgrammingLanguage:
    """Represent a Programming Language object."""

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialise a ProgrammingLanguage instance.

        name: str, name of the programming language
        typing: str, typing discipline (e.g., 'Dynamic' or 'Static')
        reflection: bool, whether the language supports reflection
        year: int, year the language first appeared
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language is dynamically typed, False otherwise."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of the ProgrammingLanguage object."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
