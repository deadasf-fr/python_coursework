#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
str_l=""
str2_l=""
str3_l=""
for letter in range(0,nr_letters):
  in1=random.choice(letters)
  str_l+=in1
for number in range(0,nr_symbols):
  in2=random.choice(numbers)
  str2_l+=in2
for symbol in range(0,nr_numbers):
  in3=random.choice(symbols)
  str3_l+=in3
combined_string = str_l + str2_l + str3_l

# Convert combined string to list of characters
combined_list = list(combined_string)

# Shuffle the list of characters
random.shuffle(combined_list)

# Join the shuffled characters to form the final password
password = ''.join(combined_list)
print(password)


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P