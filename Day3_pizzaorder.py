# Python Pizza Order Program  

print("Welcome to Python Pizza Deliveries!")  

# Get user choices for pizza size, pepperoni, and extra cheese  
size = input("What size pizza do you want? S, M or L: ")  
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")  
extra_cheese = input("Do you want extra cheese? Y or N: ")  

# Initialize bill  
bill = 0  

# Add cost based on pizza size  
if size == "S":  
    bill += 15  
elif size == "M":  
    bill += 20  
else:  
    bill += 25  

# Add cost for pepperoni  
if pepperoni == "Y":  
    if size == "S":  
        bill += 2  
    else:  
        bill += 3  

# Add cost for extra cheese  
if extra_cheese == "Y":  
    bill += 1  

# Display the final bill  
print(f"Your final bill is: ${bill}")  
