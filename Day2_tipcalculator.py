# Tip Calculator

# Welcome message
print("Welcome to the tip calculator")

# Get the total bill amount from the user
bill = float(input("Enter the bill: $ "))

# Get the tip percentage (10, 12, or 15) from the user
tip = int(input("Enter the percentage of tip that can be 10, 12, or 15: "))

# Get the number of people to split the bill
people = int(input("Enter the number of people that you want to share the bill: "))

# Calculate the total amount per person
amount = (bill * ((tip / 100) + 1) / people)

# Display the final amount per person (rounded to 2 decimal places)
print(f"Amount that each person needs to pay: ${round(amount, 2)}")
