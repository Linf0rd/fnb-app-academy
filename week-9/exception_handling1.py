# Lesson 6 - Exception Handling 

try:
    print(x)
except NameError:
    print("Variable x is not defined")
else:
    print("Eveything went wrong")


x = -1

if x < 0:
    raise ValueError("Negative value error")