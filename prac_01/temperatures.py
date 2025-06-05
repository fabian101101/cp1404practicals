"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion:
    display menu
    get choice and convert to uppercase
    while choice is not "Q"
        if choice is "C"
            get celsius temperature
            convert celsius to fahrenheit
            display fahrenheit result
        else if choice is "F"
            get fahrenheit temperature
            convert fahrenheit to celsius
            display celsius result
        else
            display invalid option message
        display menu
        get choice and convert to uppercase
    display thank you message
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        # Convert Celsius to Fahrenheit
        try:
            celsius = float(input("Celsius: "))
            fahrenheit = celsius * 9.0 / 5 + 32
            print(f"Result: {fahrenheit:.2f} F")
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "F":
        # Convert Fahrenheit to Celsius
        try:
            fahrenheit = float(input("Fahrenheit: "))
            celsius = 5 / 9 * (fahrenheit - 32)
            print(f"Result: {celsius:.2f} C")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")