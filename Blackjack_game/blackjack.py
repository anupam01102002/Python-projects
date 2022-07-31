from art import logo
from replit import clear
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []
continue_game = True

print("Simple Rules\n\n--->How do you beat the dealer?\n1.) By drawing a hand value that is higher than the dealer’s hand value\n2.) By the dealer drawing a hand value that goes over 21.\n3.) By drawing a hand value of 21 on your first two cards, when the dealer does not.\n\n--->How do you lose to the dealer? \n1.) Your hand value exceeds 21.\n2.) The dealers hand has a greater value than yours at the end of the round\n")

choice_1 = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ")
while continue_game:
    player_cards = []
    computer_cards = []
    if choice_1 == 'y':
        clear()
        print(logo)

        player_cards.append(random.choice(cards))
        player_cards.append(random.choice(cards))
        current_score_p = player_cards[0] + player_cards[1]
        print(f"Your cards: {player_cards}, current score: {current_score_p}")

        computer_cards.append(random.choice(cards))
        print(f"Dealer's first card: {computer_cards[0]}")

        choice_2 = input("Type 'y' to get another card, type 'n' to pass: ")
        if choice_2 == 'y':
            player_cards.append(random.choice(cards))
            computer_cards.append(random.choice(cards))
            current_score_c = computer_cards[0] + computer_cards[1]
            current_score_p = player_cards[0] + player_cards[1] + player_cards[2]
            print(f"Your final hand: {player_cards}, final score: {current_score_p}")
            print(f"Dealer's final hand: {computer_cards}, final score: {current_score_c}")
            
            if current_score_c > 21:
                print("You win")
            elif current_score_p > 21:
                print("You lose")
            elif current_score_c > current_score_p and current_score_c < 22:
                print("You Lose")
            elif current_score_c < current_score_p and current_score_p < 22:
                print("You Win")
            else:
                print("Error")
            
        else:
            computer_cards.append(random.choice(cards))
            
            current_score_c = computer_cards[0] + computer_cards[1]
            print(f"Your final hand: {player_cards}, final score: {current_score_p}")
            print(f"Dealer's final hand: {computer_cards}, final score: {current_score_c}")

            if current_score_c > 21:
                print("You win")
            elif current_score_p > 21:
                print("You lose")
            elif current_score_c > current_score_p and current_score_c < 22:
                print("You Lose")
            elif current_score_c < current_score_p and current_score_p < 22:
                print("You Win")
            else:
                print("Error")            
    
    choice_1 = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ")
    if choice_1 == 'n':
        continue_game = False

