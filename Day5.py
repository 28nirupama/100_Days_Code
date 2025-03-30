import random

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
images=[rock,paper,scissors]
user_choice=int(input("welcome to play rock,paper,scissors\n Type 0 for rock,1 for paper, 2 for scissors\n"))
if user_choice>=0 and user_choice<2:
    print("User choice:",images[user_choice])
computer_choice=random.randint(0,2)

print("Computer choice: ",images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("Invalid choice you lose")
elif computer_choice==user_choice:
    print("Draw! Retry")
elif computer_choice==0 and user_choice==2:
    print("You lose")
elif user_choice==1 and computer_choice==0:
    print("You win")
elif computer_choice>user_choice:
    print("You lose")
elif user_choice>computer_choice:
    print("You win")

