from card import Card
import random

class Deck:
    def __init__(self):
        self.cards = []
        self.build_deck()
        random.shuffle(self.cards)

    def build_deck(self):
        for suit in ["Spades", "Hearts", "Clubs", "Diamonds"]:
            for rank in range(2, 15):
                self.cards.append(Card(rank, suit))

    def draw_card(self):
        return self.cards.pop(0)