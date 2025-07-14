"""
CP1404/CP5632 Practical - Client program to manage a collection of Guitar objects.
Estimated time: 40 minutes
Actual time: 55 minutes
"""

from prac_06.guitar import Guitar


def main():
    """Program to collect and display a list of guitars."""
    print("My guitars!")
    guitars = []

    # Collect guitar details from user input
    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")

    # Add hardcoded guitars for testing efficiency
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.90))

    # Print all guitars with formatted output
    if guitars:
        print("\nThese are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
