from deck import Deck
from player import Player

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player_one = Player("Player One")
        self.player_two = Player("Player Two")

    def play_round(self):
        card_one = self.deck.draw_card()
        card_two = self.deck.draw_card()
        if not card_one or not card_two:
            return False
        self.compare_cards(card_one, card_two)
        print(f"Current totals - {self.player_one.name}: {self.player_one.total_score}, {self.player_two.name}: {self.player_two.total_score}")
        return True

    def compare_cards(self, card_one, card_two):
        print(f"{self.player_one.name} drew the {card_one}")
        print(f"{self.player_two.name} drew the {card_two}")

        if self.deck.ranks.index(card_one.rank) > self.deck.ranks.index(card_two.rank):
            self.player_one.add_point()
            print("Wins - player one")
        elif self.deck.ranks.index(card_one.rank) < self.deck.ranks.index(card_two.rank):
            self.player_two.add_point()
            print("Wins - player two")
        else:
            print("Equal")

    def compare_winner(self):
        if self.player_one.total_score > self.player_two.total_score:
            print("Winner of the game --- ONE")
        elif self.player_one.total_score < self.player_two.total_score:
            print("Winner of the game --- TWO")
        else:
            print("This time it's a tie")
