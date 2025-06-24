# Lesson 2: Lists in Python part 2

fruits = ["apple", "banana", "cherry"]

fruits.append("kiwi")  # Add kiwi to the end of the list
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'kiwi']

fruits.insert(1, "orange")  # Insert orange at index 1
print(fruits)  # Output: ['apple', 'orange', 'banana', 'cherry', 'kiwi']

fruits.remove("kiwi")  # Remove kiwi from the list
print(fruits)  # Output: ['apple', 'orange', 'banana', 'cherry']

fruits.sort()  # Sort the list alphabetically
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

fruits.reverse()  # Reverse the order of the list
print(fruits)  # Output: ['orange', 'cherry', 'banana', 'apple']