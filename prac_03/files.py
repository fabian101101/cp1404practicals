"""
CP1404/CP5632 - Practical 03
Writing and reading files using different techniques.
Pseudocode:
    # Task 1: Write Name
    get name
    while name is empty
        display error
        get name
    open name.txt for writing
    write name
    close file

    # Task 2: Read Name
    open name.txt for reading
    read name
    display Hi name
    close file

    # Task 3: Sum First Two Numbers
    open numbers.txt with statement
    read first line
    read second line
    convert lines to numbers
    sum numbers
    display sum

    # Task 4: Sum All Numbers
    open numbers.txt with statement
    initialize total
    for each line in file
        convert line to number
        add to total
    display total
"""
# Constants
NAME_FILE = "name.txt"
NUMBERS_FILE = "numbers.txt"

# Task 1: Write name to file
print("Task 1: Write name to file")
while True:
    name = input("Enter name: ").strip()
    if name:
        try:
            name_file = open(NAME_FILE, "w")
            name_file.write(name)
            name_file.close()
            break
        except IOError:
            print("Error writing to file.")
    else:
        print("Name cannot be empty.")

# Task 2: Read name from file
print("\nTask 2: Read name from file")
try:
    name_file = open(NAME_FILE, "r")
    name = name_file.read().strip()
    name_file.close()
    print(f"Hi {name}!")
except FileNotFoundError:
    print(f"Error: {NAME_FILE} not found.")
except IOError:
    print("Error reading file.")

# Task 3: Sum first two numbers
print("\nTask 3: Sum first two numbers")
try:
    with open(NUMBERS_FILE, "r") as numbers_file:
        first_number = int(numbers_file.readline().strip())
        second_number = int(numbers_file.readline().strip())
        result = first_number + second_number
    print(result)
except FileNotFoundError:
    print(f"Error: {NUMBERS_FILE} not found.")
except ValueError:
    print("Error: Non-numeric data in file.")
except IOError:
    print("Error reading file.")

# Task 4: Sum all numbers
print("\nTask 4: Sum all numbers")
try:
    with open(NUMBERS_FILE, "r") as numbers_file:
        total = 0
        for line in numbers_file:
            total += int(line.strip())
    print(total)
except FileNotFoundError:
    print(f"Error: {NUMBERS_FILE} not found.")
except ValueError:
    print("Error: Non-numeric data in file.")
except IOError:
    print("Error reading file.")