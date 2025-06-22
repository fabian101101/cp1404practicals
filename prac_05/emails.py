"""
CP1404/CP5632 Practical
Emails
Estimate: 20 minutes
Actual:   25 minutes
"""


def main():
    """Store emails and names in a dictionary, confirm names, and display results."""
    email_to_name = {}
    email = input("Email: ")
    while email:
        if is_valid_email(email):
            name = extract_name_from_email(email)
            if confirm_name(name):
                email_to_name[email] = name
            else:
                email_to_name[email] = input("Name: ")
        else:
            print("Invalid email format (must be like user@domain.com)")
        email = input("Email: ")

    # Print all entries
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    """Extract a name from an email address."""
    local_part = email.split('@')[0]
    parts = local_part.split('.')
    name = ' '.join(part.title() for part in parts)
    return name


def confirm_name(name):
    """Prompt to confirm the extracted name, defaulting to Yes."""
    response = input(f"Is your name {name}? (Y/n) ").lower()
    return response in ['', 'y']


def is_valid_email(email):
    """Check if the email has a valid format (user@domain.tld)."""
    parts = email.split('@')
    if len(parts) != 2 or not parts[0] or not parts[1]:
        return False
    domain_parts = parts[1].split('.')
    return len(domain_parts) >= 2 and all(domain_parts)  # Ensure non-empty domain and TLD


main()