"""
CP1404/CP5632 Practical
State names in a dictionary
"""

CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}


def main():
    """Get state abbreviation and display full state name, then list all states."""
    print(CODE_TO_NAME)
    state_code = input("Enter short state: ")
    while state_code:
        try:
            print(f"{state_code.upper()} is {CODE_TO_NAME[state_code.upper()]}")
        except KeyError:
            print("Invalid short state")
        state_code = input("Enter short state: ")

    # Print all states neatly aligned
    max_length = max(len(code) for code in CODE_TO_NAME)
    for code, name in sorted(CODE_TO_NAME.items()):
        print(f"{code:<{max_length}} is {name}")


main()