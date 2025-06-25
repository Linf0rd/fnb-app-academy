# Lesson 7: Shopping Cart Program

'''
Create a shopping cart program that will continually ask the user
for a food product and the price of that product. At the end,
show the food items and the total cost to the user.
'''

foods = []
prices = []
total = 0.0

while True:
    food = input("Enter a food product (or  press 'q' to quit): ")
    if food.lower() == 'q':
        break
    price = float(input(f"Enter the price for {food}: R"))

    foods.append(food)
    prices.append(price)

print("\n---------- YOUR CART -----------")

for food in foods:
    print(f"{food}")

for price in prices:
    total += price

print(f"\nTotal cost: R{total:.2f}")
