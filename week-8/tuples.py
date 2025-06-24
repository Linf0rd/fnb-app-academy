# Lesson 3: Tuples in Python

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)

print(my_tuple[0])  # Access the first element: Output: 1

print(my_tuple[2])  # Access the third element: Output: 3

print(my_tuple[-1])  # Access the last element: Output: 5

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

conc_tuple = tuple1 + tuple2  # Concatenate tuples

print(conc_tuple)  # Output: (1, 2, 3, 4, 5, 6)

rep_tuple = tuple1 * 3  # Repeat tuple
print(rep_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)
