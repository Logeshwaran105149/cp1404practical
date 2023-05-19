"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
LOW_BONUS = 0.10
HIGH_BONUS = 0.15
while True:
    sales = float(input("Enter sales: $"))
    if sales < 0:
        break
    if sales < 1000:
        bonus = sales * LOW_BONUS
    else:
        bonus = sales * HIGH_BONUS
    print(f"sales bonus: {bonus:.2f} C")
