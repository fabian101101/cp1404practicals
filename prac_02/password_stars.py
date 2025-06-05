"""
CP1404/CP5632 - Practical
Pseudocode for password check program:
    set MIN_LENGTH
    get password
    while password length < MIN_LENGTH
        display error message
        get password
    print asterisks equal to password length
"""

MIN_LENGTH = 5


def main():
    """Get a valid password and print asterisks for its length."""
    password = get_password()
    print_asterisks(password)


def get_password():
    """Get a password with at least MIN_LENGTH characters."""
    while True:
        password = input("Enter password: ")
        if not password:
            print("Password cannot be empty.")
        elif len(password) < MIN_LENGTH:
            print(f"Password must be at least {MIN_LENGTH} characters.")
        else:
            return password


def print_asterisks(password, symbol="*"):
    """Print specified symbol equal to password length."""
    print(symbol * len(password))


main()