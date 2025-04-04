import random  

# ASCII Art for Rock, Paper, Scissors
rock = '''  
    _______  
---'   ____)  
      (_____)  
      (_____)  
      (____)  
---.__(___)  
'''

paper = '''  
    _______  
---'   ____)____  
          ______)  
          _______)  
         _______)  
---.__________)  
'''

scissors = '''  
    _______  
---'   ____)____  
          ______)  
       __________)  
      (____)  
---.__(___)  
'''

# List to store images
images = [rock, paper, scissors]  

# User input
user_choice = int(input("Welcome to Rock, Paper, Scissors!\nType 0 for Rock, 1 for Paper, 2 for Scissors: "))  

# Check for invalid input first
if user_choice < 0 or user_choice > 2:  
    print("Invalid choice. You lose!")  
else:  
    # Display user choice
    print("User choice:", images[user_choice])  

    # Generate computer choice
    computer_choice = random.randint(0, 2)  
    print("Computer choice:", images[computer_choice])  

    # Determine the winner
    if user_choice == computer_choice:  
        print("It's a Draw! Retry.")  
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):  
        print("You Win!")  
    else:  
        print("You Lose!")  
