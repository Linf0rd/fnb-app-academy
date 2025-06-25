# Lesson 7: My modified Shopping Cart Program

import os
import re
from datetime import datetime

# Clear terminal screen
os.system('cls' if os.name == 'nt' else 'clear')

# Welcome header
print("╔" + "═" * 36 + "╗")
print("║{:^36}║".format("LINFORD'S CASH & CARRY"))
print("╚" + "═" * 36 + "╝")

# Get customer's name
customer_name = input("\nEnter your name: ")
print("\n")

foods = []
prices = []

while True:
    # Ask for food item and price
    food = input("Enter food item (or 'q' to quit): ")
    if food.lower() == 'q':
        break
    try:
        price = float(input(f"Enter the price for {food}: R"))
    except ValueError:
        print("Invalid price! Please enter a number.")
        continue

    foods.append(food)
    prices.append(price)

# Prepare receipt data
now = datetime.now()
date_str = now.strftime("%Y-%m-%d %H:%M")
file_date_str = now.strftime("%Y-%m-%d_%H-%M")
filename = f"cash_n_carry_receipt_{file_date_str}.txt"
total = sum(prices)

# Sanitize filename to prevent path traversal and invalid characters
safe_file_date_str = re.sub(r'[^A-Za-z0-9_\-]', '_', file_date_str)
filename = f"cash_n_carry_receipt_{safe_file_date_str}.txt"

# Build receipt
receipt = []
receipt.append("╔" + "═" * 36 + "╗")
receipt.append("║{:^36}║".format("LINFORD'S CASH & CARRY"))
receipt.append("║{:^36}║".format("PURCHASE RECEIPT"))
receipt.append("╠" + "═" * 36 + "╣")
receipt.append(f"║ Customer: {customer_name:<25}║")
receipt.append(f"║ Date: {date_str:<29}║")
receipt.append("╠" + "═" * 36 + "╣")
receipt.append("║{:^36}║".format("YOUR CART"))
receipt.append("╟" + "─" * 36 + "╢")

for food, price in zip(foods, prices):
    receipt.append(
        "║ {:<25} R{:>7.2f} ║".format(food, price)
    )

receipt.append("╟" + "─" * 36 + "╢")
receipt.append("║ {:<25} R{:>7.2f} ║".format("TOTAL:", total))
receipt.append("╚" + "═" * 36 + "╝")
receipt.append(
    "   Danko for your support, {}!".format(customer_name.strip().title())
)

# Print receipt
print("\n" + "=" * 40)
for line in receipt:
    print(line)
print("=" * 40)

# Save to file
with open(filename, "w", encoding="utf-8") as f:
    for line in receipt:
        f.write(line + "\n")

print(f"\nReceipt saved to file: {filename}")
