from replit import clear
from art import logo

print(logo)

new_bid = {}
print("Welcome to the secret auction.")

bidding_finished = False
while not bidding_finished:
    name = input("What is your name?: ")
    price = input("What is your bid?: $")
    new_bid[name] = price
    should_continue = input("Are there any more bidders? Type 'yes' or 'no' ")
    if should_continue == "no":
        bidding_finished = True
    else:
        clear()
winner = max(new_bid, key=new_bid.get)
print(f"{winner} has won the bidding")