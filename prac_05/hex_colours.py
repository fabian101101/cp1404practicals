"""
CP1404/CP5632 Practical
Hexadecimal color code lookup program
"""


COLOR_TO_HEX = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}


def main():
    """Prompt for color names and display their hex codes until blank input."""
    print("Available colors:", ", ".join(COLOR_TO_HEX.keys()))
    color_name = input("Enter color name: ")
    while color_name:
        try:
            print(f"{color_name.title()} is {COLOR_TO_HEX[color_name.title()]}")
        except KeyError:
            print("Invalid color name")
        color_name = input("Enter color name: ")


main()
