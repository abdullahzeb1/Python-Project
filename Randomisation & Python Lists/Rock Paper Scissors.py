import random
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
game=[rock,paper,scissors]
user_choice=int(input("select your number 0,1,2 "))
print(f"user_choice:{user_choice}")
if user_choice>=0 and user_choice<3:
    print(game[user_choice])

if user_choice == 0 or user_choice == 1 or user_choice == 2 :
    computer_choice=random.randint(0,2)
    print(f"computer_choice:{computer_choice}")
    print(game[computer_choice])

    if user_choice == 0 and computer_choice ==2:
       print("you win")
    elif user_choice == 2 and computer_choice == 0:
       print("you lose")
    elif user_choice > computer_choice:
       print("you win")
    elif user_choice < computer_choice:
       print("you lose")
    else:
        print("It's a draw")
else:
    print("Invalid number")




