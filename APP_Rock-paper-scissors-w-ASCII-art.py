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

#   a list of ASCII art to call on 
game_images = [rock, paper, scissors]

choice = int (input ("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))
if choice > 2 or choice < 0:
    print("You've entered an incorrect number")
else:
  #     print ASCII art from "game_images list" according to its index corresponding to the "choice" value
  print(game_images[choice]) 

  computer_random = random.randint (0,2)
  print(f"Computer chose: {computer_random}")
  print(game_images[computer_random])
  
  if choice == computer_random:
    print("It's a draw")
  elif (choice == 0 and computer_random == 2) or (choice == 1 and computer_random == 0) or (choice == 2 and computer_random == 1):
    print("You win!")
  else:
    print("You lose!")
