from game import Game

if __name__ == "__main__":
    game = Game()
    while True:
        continue_game = input("Do you want to play a round? (yes/no): ").strip().lower()
        if continue_game != 'yes':
            break
        if not game.play_round():
            print("No more cards left in the deck.")
            break
    game.compare_winner()
    print(f"Final totals - {game.player_one.name}: {game.player_one.total_score}, {game.player_two.name}: {game.player_two.total_score}")
    print("Game over")

