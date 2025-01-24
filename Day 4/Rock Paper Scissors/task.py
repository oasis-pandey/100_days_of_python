import random
from ctypes import c_int

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
images = [rock, paper, scissors]
computer_choice=random.randint(0,2)
user_choice = int(input("Enter 0 for rock, 1 for papers and 2 for scissors"))

print("You chose:")
print(images[user_choice])

print("Computer chose:")
print(images[computer_choice])

if user_choice == computer_choice:
    print("DRAW!")
elif user_choice == 0 and computer_choice == 1:
    print("Computer wins!")
elif user_choice == 0 and computer_choice == 2:
    print("You win")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 1 and computer_choice == 2:
    print("Computer wins")
elif user_choice == 2 and computer_choice == 0:
    print("Computer wins")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")














