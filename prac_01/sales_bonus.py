"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales_input = input("Enter sales: $")
while sales_input != "":
    try:
        sales = float(sales_input)
        if sales < 0:
            break
        if sales < 1000:
            bonus = sales * 0.10
        else:
            bonus = sales * 0.15
        print(f"Bonus: ${bonus:.2f}")
    except ValueError:
        print("Invalid input, please enter a number or press Enter to quit.")
    sales_input = input("Enter sales: $")