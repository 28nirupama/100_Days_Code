# ASCII Art for the game  
print(r'''  
*******************************************************************************  
          |                   |                  |                     |  
 _________|________________.=""_;=.______________|_____________________|_______  
|                   |  ,-"_,=""     `"=.|                  |  
|___________________|__"=._o`"-._        `"=.______________|___________________  
          |                `"=._o`"=._      _`"=._                     |  
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______  
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |  
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________  
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |  
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______  
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |  
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________  
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____  
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_  
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____  
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_  
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____  
/______/______/______/______/______/______/______/______/______/______/_____ /  
*******************************************************************************  
''')  

# Welcome message  
print("Welcome to Treasure Island.")  
print("Your mission is to find the treasure.")  

# First choice: Crossroad decision  
print("You're at the crossroad. Where do you want to go?")  
dir = input("Type 'Left' or 'Right' ")  

if dir == "Left":  
    # Second choice: Boat decision  
    print("Ohh nice. Now the boat is arriving. What do you want to do?")  
    move = input("Type 'swim' or 'wait' ")  

    if move == "wait":  
        # Third choice: Door decision  
        print("Oh nice. Which door do you want to go through?")  
        door = input("Type 'Red', 'Blue', or 'Yellow' ")  

        if door == "Yellow":  
            print("You win!")  # Winning condition  
        elif door == "Red":  
            print("Burned by fire. Game over.")  
        elif door == "Blue":  
            print("Eaten by beasts. Game over.")  
        else:  
            print("Game over.")  
    else:  
        print("Attacked by a trout. Game over.")  
else:  
    print("Fell into a hole. Game over.")  
