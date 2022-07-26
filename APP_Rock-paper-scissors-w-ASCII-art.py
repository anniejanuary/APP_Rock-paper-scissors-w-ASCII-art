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


import random

choice = int (input ("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))
if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)

print("Computer chose: ")
computer_random = random.randint (0,2)
if computer_random == 0:
  print(rock)
elif computer_random == 1:
  print(paper)
elif computer_random == 2:
  print(scissors)

if (choice == 0 and computer_random == 0) or (choice == 1 and computer_random == 1) or (choice == 2 and computer_random == 2):
  print("It's a draw")
elif (choice == 0 and computer_random == 2) or (choice == 1 and computer_random == 0) or (choice == 2 and computer_random == 1):
  print("You've won!")
else:
  print("You've lost!")
