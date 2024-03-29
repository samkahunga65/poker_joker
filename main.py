import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
pick = (0, 1)

playing = True

class Card:
    
    def __init__(self, suit, rank, pick):
        
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        
        return self.rank + ' of ' + self.suit


class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        deck_cont = ''
        for card in self.deck:
            deck_cont += '\n '+card.__str__() 
        return 'the deck contains' + deck_cont
    

    def shuffle(self):
        random.shuffle(self.deck)
        
    def top_card(self):
        return self.deck.pop()
    
    def reshuffle(self):
    	for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))



class player:

	def __init__(self):
		self.cards = []
		self.carded = True

	def add_card(self, card):
		self.cards.append(card)

