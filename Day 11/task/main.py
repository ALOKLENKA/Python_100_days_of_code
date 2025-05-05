from art import logo
import random
print(logo)

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# comp_total=0
# user_total=0
# pick_card=True
# while pick_card:
#             user_card=deal_card()
#             print(f"You have choosen: {user_card}")
#             comp_card=deal_card()
#             print(f"computer has choosen: {comp_card}")
#             user_total += user_card
#             comp_total +=comp_card
#             if user_total >21:
#               print(f"your total score is: {user_total} so you lose")
#               pick_card=False
#             elif comp_total >21:
#                 print(f"Computer's total score is: {comp_total} so you win")
#                 pick_card = False

