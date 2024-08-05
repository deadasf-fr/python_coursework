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
list=[rock,paper,scissors]
a=input("What do you choose> Type 0 for Rock, 1 for Paper or 2 for Scissors.")
if a=="0":
  print(rock)
elif a=="1":
  print(paper)
elif a=="2":
  print(scissors)
  
print("Computer chose: ")
cmp_random=random.choice(list)
print(cmp_random)
if a=="0" and cmp_random==rock:
  print("Tie")
elif a=="1" and cmp_random==rock:
  print("You win")
elif a=="2" and cmp_random==rock:
  print("You lose")
elif a=="0" and cmp_random==paper:
  print("You lose")
elif a=="1" and cmp_random==paper:
  print("Tie")
elif a=="2" and cmp_random==paper:
  print("You win")
elif a=="0" and cmp_random==scissors:
  print("You win")
elif a=="1" and cmp_random==scissors:
  print("You lose")
else:
  print("Tie")
