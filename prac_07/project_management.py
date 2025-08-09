"""
CP1404/CP5632 Practical - Project management program.
Estimated time: 3 hours
Actual time: [To be updated]
"""
from project import Project
from datetime import datetime


def load_projects(filename):
    """Load projects from a tab-delimited file into a list of Project objects."""
    projects = []
    with open(filename, 'r') as file:
        file.readline()  # Skip header
        for line in file:
            parts = line.strip().split('\t')
            name = parts[0]
            start_date = datetime.strptime(parts[1], "%d/%m/%Y").date()
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects


def save_projects(filename, projects):
    """Save projects to a tab-delimited file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    """Display incomplete and completed projects, sorted by priority."""
    incomplete = [p for p in projects if not p.is_completed()]
    completed = [p for p in projects if p.is_completed()]

    print("Incomplete projects:")
    for project in sorted(incomplete):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(completed):
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Display projects starting after a user-specified date, sorted by date."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    try:
        filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()
        filtered_projects = [p for p in projects if p.start_date > filter_date]
        for project in sorted(filtered_projects, key=lambda x: x.start_date):
            print(f"  {project}")
    except ValueError:
        print("Invalid date format. Use dd/mm/yy.")


def add_project(projects):
    """Add a new project to the list."""
    print("Let's add a new project")
    name = input("Name: ")
    while not name:
        print("Name cannot be blank.")
        name = input("Name: ")

    while True:
        date_string = input("Start date (dd/mm/yy): ")
        try:
            start_date = datetime.strptime(date_string, "%d/%m/%Y").date()
            break
        except ValueError:
            print("Invalid date format. Use dd/mm/yy.")

    priority = get_valid_number("Priority: ", is_float=False)
    cost_estimate = get_valid_number("Cost estimate: ", is_float=True)
    completion_percentage = get_valid_number("Percent complete: ", is_float=False, min_value=0, max_value=100)

    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)
    print(f"{project} added.")


def update_project(projects):
    """Update completion percentage and/or priority of a selected project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    choice = get_valid_number("Project choice: ", is_float=False, min_value=0, max_value=len(projects) - 1)
    project = projects[choice]
    print(project)

    new_percentage = input("New Percentage: ")
    if new_percentage:
        project.completion_percentage = get_valid_number("New Percentage: ", is_float=False, min_value=0, max_value=100,
                                                         default=int(new_percentage))

    new_priority = input("New Priority: ")
    if new_priority:
        project.priority = get_valid_number("New Priority: ", is_float=False, default=int(new_priority))


def get_valid_number(prompt, is_float=False, min_value=None, max_value=None, default=None):
    """Get a valid number from user input with optional range validation."""
    while True:
        try:
            if default is not None:
                return default
            value = input(prompt)
            if not value and default is None:
                return None
            value = float(value) if is_float else int(value)
            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"Value must be at most {max_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input; enter a valid number.")


def get_valid_yes_no(prompt):
    """Get a valid 'y' or 'n' response from user input."""
    while True:
        choice = input(prompt).lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        print("Please enter 'y' or 'n'.")


def main():
    """Main program to manage projects."""
    filename = "projects.txt"
    projects = load_projects(filename)
    print(f"Welcome to Pythonic Project Management\nLoaded {len(projects)} projects from {filename}")

    menu = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""

    while True:
        print(menu)
        choice = input(">>> ").lower()

        if choice == 'l':
            new_filename = input("Enter filename to load: ")
            projects = load_projects(new_filename)
            print(f"Loaded {len(projects)} projects from {new_filename}")

        elif choice == 's':
            new_filename = input("Enter filename to save: ")
            save_projects(new_filename, projects)
            print(f"Saved {len(projects)} projects to {new_filename}")

        elif choice == 'd':
            display_projects(projects)

        elif choice == 'f':
            filter_projects_by_date(projects)

        elif choice == 'a':
            add_project(projects)

        elif choice == 'u':
            update_project(projects)

        elif choice == 'q':
            if get_valid_yes_no(f"Would you like to save to {filename}? "):
                save_projects(filename, projects)
                print(f"Saved {len(projects)} projects to {filename}")
            print("Thank you for using the custom-built project management software.")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()