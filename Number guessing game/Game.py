from random import *
print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")
Number = randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy or 'hard': ")
won = False
if difficulty == "easy":
    i = 10
    while i > 0 and won == False:
        guess = int(input("make a guess: "))
        i -= 1
        if guess < Number:
            print(
                f"Too Low\nYou have {i} attempts remaining to guess the number")
        elif guess > Number:
            print(
                f"Too High\nYou have {i} attempts remaining to guess the number")
        elif guess == Number:
            print("You have made the right guess")
            won = True

elif difficulty == "hard":
    i = 5
    while i > 0 and won == False:
        guess = int(input("make a guess: "))
        i -= 1
        if guess < Number:
            print(
                f"Too Low\nYou have {i} attempts remaining to guess the number")
        elif guess > Number:
            print(
                f"Too High\nYou have {i} attempts remaining to guess the number")
        elif guess == Number:
            print("You have made the right guess")
            Won = True
