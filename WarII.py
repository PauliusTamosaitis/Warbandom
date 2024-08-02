import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rank_name = self.rank
        if self.rank == 11:
            rank_name = "Jack"
        elif self.rank == 12:
            rank_name = "Queen"
        elif self.rank == 13:
            rank_name = "King"
        elif self.rank == 14:
            rank_name = "Ace"
        return f"{rank_name} of {self.suit}"

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

class Player:
    def __init__(self, name):
        self.name = name

    def add_point(self):
        self.total_score += 1
        self.total_score = 0

    def add_point(self):
        self.total_score += 1

