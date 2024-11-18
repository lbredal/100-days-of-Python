# The Secret Auction Program

from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

other_bidders = True

bids = {}

while(other_bidders):
    name = input("What is your name?")
    bid = int(input("What is your bid price?"))

    bids[name] = bid

    other = input("Are there other bidders ? yes/no")

    if other == "no":
        other_bidders = False

    clear()

highest_bidder = ""
highest_bid = 0

for bidder in bids:
    if(bids[bidder] > highest_bid):
        highest_bid = bids[bidder]
        highest_bidder = bidder

print(f"The winner is {highest_bidder} with a bid of {highest_bid}")