""" Day 11 - Blackjack
Chose your difficulty
Normal 😎: Use all Hints below to complete the project.
Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
Expert 🤯: Only use Hint 1 to complete the project.
Our Blackjack Game House Rules
The deck is unlimited in size.
There are no jokers.
The Jack/Queen/King all count as 10.
The Ace can count as 11 or 1.
Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

The cards in the list have equal probability of being drawn.
Cards are not removed from the deck as they are drawn.
The computer is the dealer.
"""

from art import logo
import random
print(logo)

 

def play_game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    game_is_finished = False
    another_card = "y"
    #computer hand
    computer_hand = []
    computer_hand.append(random.choice(cards))

    #player hand
    player_hand = []    
    player_hand.append(random.choice(cards))

    
# må skrive om her - while-løkken må sjekke om game_is_finished, og det å spørre om kort må være en if-setning inne i while-løkken
    while(another_card == "y"):
        player_hand.append(random.choice(cards))
        player_score = sum(cards)
        print(f"Your cards: {player_hand} , current score: {player_score}")    
        print(f"Computer's first card: {computer_hand[0]}")

        another_card = input("Type 'y' to get another card, type 'n' to pass:")

        if(another_card == "y"):
            player_hand.append(random.choice(cards))
            player_score = sum(cards)
            if (player_score > 21):
                game_is_finished = True


play_game()