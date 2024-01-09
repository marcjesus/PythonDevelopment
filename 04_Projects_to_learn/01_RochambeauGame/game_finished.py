import random

# List of possible moves
MOVES = ['rock', 'paper', 'scissors']

class Player:
    """Parent class representing a player in the game."""

    def move(self):
        """Abstract method for getting the player's move."""
        pass

    def learn(self, my_move, their_move):
        """Records the player's and opponent's moves."""
        self.player_move = my_move
        self.opponent_move = their_move

    def get_opponent_move(self, move2):
        """Sets the opponent's move."""
        self.opponent_move = move2.get_move()


def beats(one, two):
    """Determines the winner between two moves."""
    if ((one == 'rock' and two == 'scissors') or 
        (one == 'scissors' and two == 'paper') or 
        (one == 'paper' and two == 'rock')):
        return 1
    elif ((two == 'rock' and one == 'scissors') or 
          (two == 'scissors' and one == 'paper') or 
          (two == 'paper' and one == 'rock')):
        return 2
    elif one == two:
        return 0
    else:
        print("ERROR in beats")


class RandomPlayer(Player):
    """Represents a player making random moves."""

    def move(self):
        """Generates a random move among 'rock', 'paper', or 'scissors'."""
        value = random.randint(0, 2)
        if value == 0:
            return 'rock'
        elif value == 1:
            return 'paper'
        else:
            return 'scissors'


class HumanPlayer(Player):
    """Represents a human player inputting moves."""

    def move(self):
        """Prompts the user for a move and returns the selected move."""
        while True:
            entry = input("Do you play rock, paper or scissors?")
            if entry in MOVES:
                return entry
            else:
                print("You didn't select anything, try again")


class ReflectPlayer(Player):
    """Represents a player that reflects the opponent's previous move."""

    def move(self):
        """Reflects the opponent's last move or chooses randomly."""
        if hasattr(self, 'opponent_move') and self.opponent_move in MOVES:
            index = MOVES.index(self.opponent_move)
            return MOVES[(index + 1) % len(MOVES)]
        else:
            return MOVES[random.randint(0, 2)]


class Game:
    """Manages the Rock, Paper, Scissors game between two players."""

    def __init__(self, p1, p2):
        """Initializes the game with two player instances."""
        self.p1 = p1
        self.p2 = p2
        self.score_player1 = 0
        self.score_player2 = 0

    def play_round(self):
        """Executes a single round of the game."""
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You: {move1}  Computer: {move2}")
        result = beats(move1, move2)
        if result == 1:
            self.score_player1 += 1
        elif result == 2:
            self.score_player2 += 1
        else:
            return 0
        print(f"Player : {self.score_player1} | Computer : {self.score_player2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        """Initiates and plays the entire game."""
        print("Game start!")
        for _ in range(3):
            print("=====================================================")
            print(f"Round {_}:")
            self.play_round()

        if self.score_player1 > self.score_player2:
            print("YOU WIN")
        elif self.score_player1 < self.score_player2:
            print("COMPUTER WINS")
        else:
            print("DRAW")
        print("Game over!")


if __name__ == '__main__':
    # Set up players and start the game
    player1 = HumanPlayer()
    player2 = ReflectPlayer()
    game = Game(player1, player2)
    game.play_game()
