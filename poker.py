#!/usr/bin/evn python3

"""
poker.py
final independant project for atcs 2024
trying to create a poker class 
"""

__author__ = "Junaid Bhatti"
__version__ = "2024-02-01"

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


class Deck:
    def __init__(self):
        self.cards = [] #list to store the cards
        for suit in ['Spades', 'Clubs', 'Hearts', 'Diamonds']: #creating numbered cards between 2-10 and putting them in the deck
            for value in range[2,11]:
                self.cards.append(Card(suit, str(value)))
            for rank in ['Jack', 'Queen', 'King', 'Ace']: #creating face cards and adding them to deck

    def deal_cards(self):
    
    def shuffle(self):


class Hand:
    def printhand

class Game:







def main():
    # The program goes here

if __name__ == "__main__":
    main()


    