import random
rock = '''
    _______
---'   ____)
      (_____)
 Rock (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
 Paper    _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
 Scissor __________)
      (____)
---.__(___)
'''

game_image = [rock, paper, scissors]
print("Welcome to Rock, Papaer, Scissor game !")
user_option=input("Enter your choice between Rock, Paper, Scissor:")
if user_option.lower() == "rock":
    user_choice =0
elif user_option.lower() == "paper":
    user_choice =1
elif user_option.lower() == "scissor":
    user_choice = 2
else:
    print("Invalid choice , You lose !Valid choices are Rock, Paper, Scissor:")
    exit()
# if user_choice <0 or user_choice >=3:
#     print("Invalid choice , please enter either 0 or 2")
#     exit()

print(f"You have choosen {game_image[user_choice]}")
computer_choice=random.randint(0,2)
print(f"Computer has choosen {game_image[computer_choice]}")

if user_choice==computer_choice:
    print("So its a draw")
elif user_choice ==2 and computer_choice==0:
    print("So you lose")
elif computer_choice==2 and user_choice==0:
    print("So you win")
elif user_choice > computer_choice:
    print("So you Win")
elif computer_choice > user_choice:
    print("So You lose")


