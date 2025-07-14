"""
CP1404/CP5632 Practical - Test program for Guitar class.
Estimated time: 20 minutes
Actual time: 25 minutes
"""

from prac_06.guitar import Guitar


def main():
    """Test the get_age() and is_vintage() methods of the Guitar class."""
    # Create two Guitar objects for testing
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 1512.90)

    # Test get_age() for guitar1
    expected_age1 = 103  # 2025 - 1922
    actual_age1 = guitar1.get_age()
    print(f"{guitar1.name} get_age() - Expected {expected_age1}. Got {actual_age1}")

    # Test get_age() for guitar2
    expected_age2 = 12  # 2025 - 2013
    actual_age2 = guitar2.get_age()
    print(f"{guitar2.name} get_age() - Expected {expected_age2}. Got {actual_age2}")

    # Test is_vintage() for guitar1
    expected_vintage1 = True  # Age 103 >= 50
    actual_vintage1 = guitar1.is_vintage()
    print(f"{guitar1.name} is_vintage() - Expected {expected_vintage1}. Got {actual_vintage1}")

    # Test is_vintage() for guitar2
    expected_vintage2 = False  # Age 12 < 50
    actual_vintage2 = guitar2.is_vintage()
    print(f"{guitar2.name} is_vintage() - Expected {expected_vintage2}. Got {actual_vintage2}")


main()
