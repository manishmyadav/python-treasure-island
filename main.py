print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

message0 = 'You are at a cross road. Where do you want to go? Type "left" or "right".\n'
crossroad_choice = input(message0).lower()

if crossroad_choice == 'left':
  message1 = "You came to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n"
  swim_or_wait_choice = input(message1).lower()
  if swim_or_wait_choice == "wait":
    message2 = 'You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour door would you choose to enter? R, Y or B?\n'
    door_choice = input(message2).lower()
    if door_choice == "r":
      print("Its a room full of fire. Game Over.")
      print("Better luck next time. :)")
    elif door_choice == "y":
      print("Voila! You found the Treasure! You WIN.")
    elif door_choice == 'b':
      print("You enter a room of beasts. Game Over.")
      print("Better luck next time. :)")
    else:
      print("You choose a door that doesn't exist. Game Over.")
  elif swim_or_wait_choice == "swim":
    print("You are attacked by an angry trout! Game Over.")
    print("Better luck next time.")
  else:
    print("You made an invalid choice. Game Over.")
elif crossroad_choice == 'right':
  print("You fell into the Hole. Game Over.")
  print("Better luck next time.")
else:
  print("You made an invalid choice. Game Over.")