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

game_images = [rock, paper, scissors] # ASCII art as a list indexes to call on

choice = int (input ("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))
if choice > 2 or choice < 0:
    print("You've entered an incorrect number")
else:
  print(game_images[choice]) # print "game_image list" item no "choice"

computer_random = random.randint (0,2)
print(f"Computer chose: {computer_random}")
print(game_images[computer_random])

if choice == computer_random:
  print("It's a draw")
elif (choice == 0 and computer_random == 2) or (choice == 1 and computer_random == 0) or (choice == 2 and computer_random == 1):
  print("You win!")
else:
  print("You lose!")
