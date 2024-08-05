def name_value(name):
    value = 0
    for char in name.lower():
        if char.isalpha():
            value += ord(char) - ord('a') + 1
    return value

# Example usage:
name = "Zelle"
print("The value of the name", name, "is", name_value(name))
