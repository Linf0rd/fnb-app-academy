# Lesson 1 - Introduction to Functions

def greet(name):
    """Function to greet a user by name."""
    print(f"Hello, {name}! Welcome to the program.")

    greet("Alice")


def add(a, b):
    """Function to add two numbers."""
    return a + b

    result = add(2, 5)
    print(result)


def factorial(n):
    """Function to calculate the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def greet_with_greeting(name, greeting="Hello"):
    """Function to greet a user with a custom greeting."""
    print(f"{greeting}, {name}!")

    greet_with_greeting("Bob", "Good morning")
