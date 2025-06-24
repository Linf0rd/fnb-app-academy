# Lesson 4: Sets in Python

'''
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

my_set.add(6)  # Add an element
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

my_set.remove(3)  # Remove an element
print(my_set)  # Output: {1, 2, 4, 5, 6}
'''

set1 = {1, 2, 3}
set2 = {4, 5, 6}

# Union

union_set = set1.union(set2)  # Union of sets
print(union_set)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection
inter_set = set1.intersection(set2)  # Intersection of sets
print(inter_set)  # Output: set() (empty set, no common elements)

# Difference
diff_set = set1.difference(set2)  # Elements in set1 not in set
print(diff_set)  # Output: {1, 2, 3}
