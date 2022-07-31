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
game_images = [rock, paper, scissors]

user_input = int(input("What do You Choose? type 0 for Rock, 1 For Paper, 2 For Scissors"))

Computer_input = random.choice(game_images)

if user_input ==  0:
    print(rock)
    if Computer_input == "rock":
        print("computer choose rock\n" + rock + "\n It's a Tie")
    elif Computer_input == "Paper":
        print("computer choose paper\n" + paper + "\n You Lost")
    else:
        print("computer choose scissors\n" + scissors + "\n You Won")
elif user_input ==  1:
    print(paper)
    if Computer_input == "rock":
        print("computer choose rock\n" + rock + "\n You Won")
    elif Computer_input == "Paper":
        print("computer choose paper\n" + paper + "\n It's a Tie")
    else:
        print("computer choose scissors\n" + scissors + "\n You Lost")
elif user_input ==  2:
    print(scissors)
    if Computer_input == "rock":
        print("computer choose rock\n" + rock + "\n You Lost")
    elif Computer_input == "Paper":
        print("computer choose paper\n" + paper + "\n You Won")
    else:
        print("computer choose scissors\n" + scissors + "\n It's a Tie")
    



