"""
CP1404/CP5632 Practical
Debugging exercise: almost-working version of a CSV scores file program.
The scores.csv file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""


def main():
    """Read and display student scores from scores file in a formatted table."""
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    subjects = scores_data[0].strip().split(",")[1:]  # Skip first column if it's a header like 'Student'
    score_values = []

    # Convert each line of scores to a list of integers
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")[1:]  # Skip first column if it's a name/ID
        score_numbers = [int(value) for value in score_strings]
        score_values.append(score_numbers)

    scores_file.close()

    # Transpose to get scores per subject
    subject_scores = list(zip(*score_values))  # Convert rows (students) to columns (subjects)

    # Print formatted table
    print("\n{:<10} {:<45} {:<10} {:<10} {:<10}".format("Subject", "Scores", "Max", "Min", "Average"))
    print("-" * 90)
    for i, subject in enumerate(subjects):
        scores = list(subject_scores[i])
        max_score = max(scores)
        min_score = min(scores)
        avg_score = sum(scores) / len(scores)
        # Format scores as a comma-separated string
        scores_str = ", ".join(str(score) for score in scores)
        print(f"{subject:<10} {scores_str:<45} {max_score:<10} {min_score:<10} {avg_score:<10.2f}")


main()
