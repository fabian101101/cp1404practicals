"""
CP1404/CP5632 Practical
Data file -> lists program
"""

filename = "subject_data.txt"


def main():
    """Load and display subject data from file."""
    data = load_data()
    print(data)
    display_subject_details(data)


def load_data():
    """Read data from file and return as a list of lists: [subject, lecturer, students]."""
    subject_data = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()  # Remove the \n
            parts = line.split(',')  # Separate the data into its parts
            parts[2] = int(parts[2])  # Convert number of students to integer
            subject_data.append(parts)  # Add the processed parts to the list
    return subject_data


def display_subject_details(data):
    """Display subject details in a formatted way."""
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


main()
