"""
CP1404/CP5632 Practical
Basic list operations and woefully inadequate security checker
"""


def main():
    """Check if a username is in the authorized list."""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
                 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    username = input("Enter your username: ")
    if username in usernames:
        print("Access granted")
        get_numbers_and_display_info()
    else:
        print("Access denied")


def get_numbers_and_display_info():
    """Prompt for 5 numbers and display statistics."""
    numbers = []
    for i in range(5):
        number = float(input("Number: "))
        numbers.append(number)

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


main()
