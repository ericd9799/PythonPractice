#! /usr/bin/python3



class Card():
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return "Card is a {} and {} value.".format(self.suit, self.value)

class Deck():
    def __init__(self):
        self.deck = []
        for
