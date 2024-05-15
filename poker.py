#!/usr/bin/evn python3

"""
poker.py
final independant project for atcs 2024
trying to create a poker class 
"""

__author__ = "Junaid Bhatti"
__version__ = "2024-02-01"

import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


class Deck:
    def __init__(self):
        self.cards = [] #list to store the cards
        #need to create a standardized deck of 52 playing cards
        #seperating them between numbered cards and face cards
        for suit in ['Spades', 'Clubs', 'Hearts', 'Diamonds']: #creating numbered cards between 2-10 and putting them in the deck
            for value in range[2,11]:
                self.cards.append(Card(suit, str(value)))
            for rank in ['Jack', 'Queen', 'King', 'Ace']: #creating face cards and adding them to deck
                self.cards.append(Card(suit,rank))

    def deal_cards(self):
        #if the deck is not empty, deal one from the top of the deck
        #if its empty return none + printstatement, if not return the card
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            return None + "There are no more cards, you need to reshuffle"
        
    def shuffle(self):
        #randomly shuffling the cards
        random.shuffle(self.cards)

class Hand:
    def 

class Game:







def main():
    # The program goes here

if __name__ == "__main__":
    main()


    