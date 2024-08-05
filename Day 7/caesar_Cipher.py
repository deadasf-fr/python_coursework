def caesar_cipher(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = ord(char) + key
            if char.islower():
                if shift > ord('z'):
                    shift -= 26
                elif shift < ord('a'):
                    shift += 26
            elif char.isupper():
                if shift > ord('Z'):
                    shift -= 26
                elif shift < ord('A'):
                    shift += 26
            result += chr(shift)
        else:
            result += char
    return result

# Example usage:
plaintext = "Sourpuss"
key = 2
encoded = caesar_cipher(plaintext, key)
decoded = caesar_cipher(encoded, -key)
print("Encoded:", encoded)
print("Decoded:", decoded)
