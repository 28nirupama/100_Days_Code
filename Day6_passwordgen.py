import random

# List of characters to choose from
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome message
print("Welcome to the PyPassword Generator!")

# Taking user input for number of letters, symbols, and numbers in the password
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Empty list to store chosen characters
pass_list = []

# Add random letters to password list
for char in range(1, nr_letters + 1):
    pass_list += random.choice(letters)

# Add random numbers to password list
for num in range(1, nr_numbers + 1):
    pass_list += random.choice(numbers)

# Add random symbols to password list
for sym in range(1, nr_symbols + 1):
    pass_list += random.choice(symbols)

# Show password list before shuffling (for debugging or learning purpose)
print("Before shuffling:", pass_list)

# Shuffle the list to make the order random
random.shuffle(pass_list)

# Show password list after shuffling
print("After shuffling:", pass_list)

# Convert list into a string (final password)
pass_v = ""
for char in pass_list:
    pass_v += char

# Print the final generated password
print("Your password is:", pass_v)
