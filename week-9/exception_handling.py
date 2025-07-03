# Lesson 5 - Exception Handling

"""
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("An exception occurred")
"""

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("Execution completed, regardless of success or failure")
