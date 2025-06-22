"""
CP1404/CP5632 Practical
Word Occurrences
Estimate: 20 minutes
Actual:   25 minutes
"""


def main():
    """Count word occurrences in a user-provided string and display sorted, aligned output."""
    text = input("Text: ")
    word_to_count = {}

    # Split text into words and count occurrences
    for word in text.split():
        word_to_count[word] = word_to_count.get(word, 0) + 1

    # Find the longest word for alignment
    max_length = max(len(word) for word in word_to_count) if word_to_count else 0

    # Print sorted words with aligned counts
    for word in sorted(word_to_count):
        print(f"{word:<{max_length}} : {word_to_count[word]}")


main()
