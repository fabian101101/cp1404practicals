"""
CP1404/CP5632 Practical - Client program to use the ProgrammingLanguage class.
Estimated time: 20 minutes
Actual time: 15 minutes
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """Demo test code to show how to use ProgrammingLanguage class."""
    # Create ProgrammingLanguage objects
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Print the python object to test __str__ method
    print(python)

    # Create a list of ProgrammingLanguage objects
    languages = [python, ruby, visual_basic]

    # Print names of dynamically typed languages
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
