# Lesson 2 - Math Operations

def add(a, b):
    """Function to add two numbers."""
    return a + b


def subtract(a, b):

    """Function to subtract two numbers."""
    return a - b


def multiply(a, b):
    """Function to multiply two numbers."""
    return a * b


def divide(a, b):
    """Function to divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def modulus(a, b):
    """Function to find the modulus of two numbers."""
    return a % b


def power(a, b):
    """Function to raise a number to a power."""
    return a ** b


def square_root(a):
    """Function to find the square root of a number."""
    if a < 0:
        raise ValueError("Cannot find the square root of a negative number.")
    return a ** 0.5
