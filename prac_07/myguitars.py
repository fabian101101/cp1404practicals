"""
CP1404/CP5632 Practical - Guitar management program.
Estimated time: 1 hour
Actual time: 1 hour 15 minutes
"""
from guitar import Guitar


def load_guitars(filename):
    """Load guitars from a CSV file into a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    """Display all guitars in the list."""
    for guitar in guitars:
        print(guitar)


def add_guitar(guitars):
    """Prompt user to add a new guitar and append it to the list; return False if blank name entered."""
    name = input("Name: ")
    if not name:
        return False
    year = get_valid_number("Year: ", is_float=False, is_year=True)
    cost = get_valid_number("Cost: ", is_float=True)
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{guitar} added.")
    return True


def get_valid_number(prompt, is_float=False, is_year=False):
    """Get a valid number (integer or float) from user input; validate year if specified."""
    while True:
        try:
            value = input(prompt)
            if is_float:
                value = float(value)
                if value < 0:
                    print("Cost cannot be negative.")
                    continue
                return value
            else:
                value = int(value)
                if is_year:
                    if not (1900 <= value <= 2025):
                        print("Year must be a four-digit number between 1900 and 2025.")
                        continue
                return value
        except ValueError:
            print("Invalid input; enter a valid number.")


def save_guitars(filename, guitars):
    """Save all guitars to the CSV file."""
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


def main():
    """Main program to manage guitars."""
    filename = "guitars.csv"
    guitars = load_guitars(filename)

    print("My guitars!")
    print("\n... Loaded guitars:")
    display_guitars(guitars)

    print("\n... Sorted by year:")
    guitars.sort()
    display_guitars(guitars)

    print("\nAdd new guitars (enter a blank name to finish):")
    while add_guitar(guitars):
        pass

    print("\n... Final guitar list:")
    display_guitars(guitars)

    save_guitars(filename, guitars)
    print(f"\nGuitars saved to {filename}")


if __name__ == "__main__":
    main()
