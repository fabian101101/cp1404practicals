"""
Program to calculate the total price for a number of items.
If the total is over $100, a 10% discount is applied.
Keeps asking for a valid number of items if a negative or invalid input (including empty) is entered.
"""
# Get a valid number of items
while True:
    try:
        items_input = input("Number of items: ")
        num_items = int(items_input)  # Try to convert input to an integer
        if num_items < 0:
            print("Invalid number of items!")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")  # Handles empty input or non-numeric input

# Get price for each item
total_price = 0
for i in range(num_items):
    while True:
        try:
            price = float(input(f"Price of item {i + 1}: "))
            total_price += price
            break
        except ValueError:
            print("Please enter a valid price.")

# Apply 10% discount if total is over $100
if total_price > 100:
    total_price = total_price * 0.9

# Show the final total
print(f"Total price for {num_items} items is ${total_price:.2f}")