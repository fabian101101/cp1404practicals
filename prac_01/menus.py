"""
CP1404/CP5632 - Practical
Menu-driven program to greet the user or say goodbye based on their choice.
Pseudocode:

get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message

"""

# Get name from the user
name = input("Enter name: ")

# Display the menu
MENU = """(H)ello
(G)oodbye
(Q)uit"""

print(MENU)

# Get the user's choice
choice = input(">>> ").upper()

# Process the choice until the user chooses to quit
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    # Display the menu again
    print(MENU)
    # Get the user's choice again
    choice = input(">>> ").upper()

# Display the finished message
print("Thank you.")
