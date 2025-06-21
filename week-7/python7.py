# Loop Control Statements

# Example 1 - Break Statement
fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    if fruit == "cherry":
        break  # Exit the loop when "cherry" is encountered
    print(fruit)  # Output: apple, banana (each on a new line)

print()


# Example 2 - Continue Statement
for fruit in fruits:
    if fruit == "cherry":
        continue  # Skip the iteration when "cherry" is encountered
    print(fruit)  # Output: apple, banana, date (each on a new line)
print()


# Example 3 - Pass Statement
for fruit in fruits:
    if fruit == "cherry":
        pass  # Do nothing for "cherry"
    print(fruit)  # Output: apple, banana, cherry, date (each on a new line)


# Example 4 - Break in Nested Loops

count = 0

while count < 5:
    print("Outer loop iteration:", count)
    count += 1
    if count == 3:
        break  # Exit the outer loop when count is 3