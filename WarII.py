
from card import Card
from deck import Deck
from player import Player

class Game:

    def __init__(self):
        self.deck = Deck()
        self.player_one = Player("Player One")
        self.player_two = Player("Player Two")

    def play_game(self):
        while len(self.deck.cards) != 0:
            card_one = self.deck.draw_card()
            card_two = self.deck.draw_card()
            self.compare_cards(card_one, card_two)
            print(f"Current totals - {self.player_one.name}: {self.player_one.total_score}, {self.player_two.name}: {self.player_two.total_score}")

        self.compare_winner()
        print(f"Final totals - {self.player_one.name}: {self.player_one.total_score}, {self.player_two.name}: {self.player_two.total_score}")
        print("Game over")

    def compare_cards(self, card_one, card_two):
        print(f"{self.player_one.name} drew the {card_one}")
        print(f"{self.player_two.name} drew the {card_two}")

        if card_one.rank > card_two.rank:
            self.player_one.add_point()
            print("Wins - player one")
        elif card_one.rank < card_two.rank:
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

if __name__ == "__main__":
    game = Game()
    game.play_game()