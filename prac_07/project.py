"""
CP1404/CP5632 Practical - Project class.
"""
from datetime import date


class Project:
    """Represent a project with name, start date, priority, cost estimate, and completion percentage."""

    def __init__(self, name="", start_date=None, priority=1, cost_estimate=0.0, completion_percentage=0):
        """Initialize a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return string representation of the Project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, "
                f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Compare projects by priority for sorting."""
        return self.priority < other.priority

    def is_completed(self):
        """Return True if project is 100% complete, False otherwise."""
        return self.completion_percentage == 100