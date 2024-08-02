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


