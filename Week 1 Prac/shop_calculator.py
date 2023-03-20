DISCOUNT_PRICE = 100
DISCOUNT_PERCENTAGE = 0.9

num_items = int(input("Number of items:"))
while num_items < 0:
    print("Invalid number of items!")
    num_items = int(input("Number of items:"))

total_price = 0
for i in range(num_items):
    price_item = float(input("Price of item:"))
    total_price += price_item

if total_price > DISCOUNT_PRICE:
    total_price = total_price * DISCOUNT_PERCENTAGE
print(f"Total price for {num_items} items is ${total_price:.2f}")