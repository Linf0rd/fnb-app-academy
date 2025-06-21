# Lesson 8: Control Statements

# Example 1 - If Statement

num = 10

if num > 0:
    print("The number is positive")  # Output: The number is positive


# Example 2

num1 = 130

if num1 > 0:
    print("The number is positive")  # Output: The number is positive


# Example 3 - If-Else Statement

num2 = -5

if num2 > 0:
    print("The number is positive")  # No output, as the condition is false
else:
    print("The number is either zero or negative")  # Output: The number is either zero or negative


# Example 4 - If-Elif-Else Statement

num3 = -5

if num3 > 0:
    print("The number is positive")  # No output, as the condition is false
elif num3 == 0:
    print("The number is zero") # No output, as the condition is false
else:
    print("The number is negative") # Output: The number is negative

