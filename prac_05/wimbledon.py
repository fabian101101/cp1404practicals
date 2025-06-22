"""
CP1404/CP5632 Practical
Wimbledon
Estimate: 30 minutes
Actual:   35 minutes
"""


def main():
    """Read Wimbledon data and display champions and countries."""
    records = load_data("wimbledon.csv")
    champion_to_wins = count_champions(records)
    countries = get_countries(records)
    display_results(champion_to_wins, countries)


def load_data(filename):
    """Read CSV file and return list of lists."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Skip header
        for line in in_file:
            records.append(line.strip().split(","))
    return records


def count_champions(records):
    """Count wins for each champion using a dictionary."""
    champion_to_wins = {}
    for record in records:
        champion = record[2]  # Champion column
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins


def get_countries(records):
    """Get unique countries in alphabetical order using a set."""
    countries = set(record[1] for record in records)  # Country column
    return sorted(countries)


def display_results(champion_to_wins, countries):
    """Display champions with win counts and countries."""
    print("Wimbledon Champions:")
    for champion, wins in sorted(champion_to_wins.items()):
        print(f"{champion} {wins}")
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


main()
