#tip calculator
print("Welcome to the tip calculator")
bill=float(input("Enter the bill:$ "))
tip=int(input("Enter the percentage of tip that can be 10,12,15 per:"))
people=int(input("Enter the number of people that you want to share the bill:"))
amount=(bill*((tip/100)+1)/people)
print(f"amount that shared:${round(amount,2)}")