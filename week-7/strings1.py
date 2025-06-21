# Lesson 3: Advanced concepts - Strings

# Example 1 - Accessing characters in a string

message = 'Hello'

print(message[0]) # First character
print(message[1]) # Second character

print(message[-1]) # Last character


# Example 2 - String length

print(len(message))


# Example 3 - String length with spaces

message_with_spaces = ' Hello '

print(len(message_with_spaces))


# Example 4 - Remove leading and trailing whitespaces

message_with_spaces1 = ' Hello World! '

print(message_with_spaces1.strip()) # Removes leading and trailing whitespaces
print(message.lower()) # Converts to lowercase
print(message.split(', ')) # Splits the string into a list on the comma