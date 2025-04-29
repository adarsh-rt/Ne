import random

class Ludo:
    def __init__(self):
        self.players = {1: 0, 2: 0}  # Player positions
        self.winner = None

    def roll_dice(self):
        return random.randint(1, 6)

    def move_player(self, player, steps):
        if self.players[player] + steps <= 30:  # Assuming 30 is the end position
            self.players[player] += steps
        if self.players[player] == 30:
            self.winner = player

    def play(self):
        while self.winner is None:
            for player in self.players.keys():
                input(f"Player {player} ka turn. Dice roll karne ke liye Enter dabayein...")
                steps = self.roll_dice()
                print(f"Player {player} ne {steps} roll kiya.")
                self.move_player(player, steps)
                print(f"Player {player} ki position: {self.players[player]}")
                if self.winner:
                    print(f"Player {self.winner} jeet gaya!")
                    break

if __name__ == "__main__":
    game = Ludo()
    game.play()