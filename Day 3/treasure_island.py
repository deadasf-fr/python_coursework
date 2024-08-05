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
print("Your misson is to find the treasure.")
a=input("Yourre at a cross road. Where do you want to go? Type \"left\" or \"right\" ")
a_lower=a.lower()
if a_lower=="left":
  b=input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.')
  b_lower=b.lower()
  if b_lower=="wait":
    c=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?")
    c_lower=c.lower()
    if c_lower=="red":
      print("Burnedd by fire. Game Over.")
    elif c_lower=="blue":
      print("Eaten by beasts. Game over")
    elif c_lower=="yellow":
      print("You win!")
    else:
      print("Game Over")
  elif b_lower=="swim":
    print("Attacked by trout. Game Over")
  else:
    print("Attacked by trout. Game Over")

elif a_lower=="right":
  print("Fall into a hole Game Over")
else:
  print("Fall into a hole")


