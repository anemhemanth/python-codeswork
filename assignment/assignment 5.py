from abc import ABC, abstractmethod
import random

# Base User class
class User:
    def __init__(self, username, email):
        self._username = username
        self._email = email

    def display_info(self):
        return f"User: {self._username}, Email: {self._email}"


# Player subclass
class Player(User):
    _id_counter = 1

    def __init__(self, username, email):
        super().__init__(username, email)
        self._player_id = Player._id_counter
        Player._id_counter += 1
        self._score = 0

    def update_score(self, points):
        self._score += points

    def display_info(self):
        return f"Player {self._player_id}: {self._username}, Score: {self._score}"

    def get_score(self):
        return self._score

    def get_name(self):
        return self._username


# Admin subclass
class Admin(User):
    def create_game(self):
        print("Admin created a new game!")

    def ban_player(self, player):
        print(f"Player {player.get_name()} has been banned.")


# Abstract Game class
class Game(ABC):
    def __init__(self, game_id, players):
        self._game_id = game_id
        self._players = players
        self._status = "Not Started"

    @abstractmethod
    def start_game(self):
        pass


# Concrete game classes
class ChessGame(Game):
    def start_game(self):
        self._status = "Finished"
        winner = random.choice(self._players)
        return f"Chess Game Over! Winner: {winner.get_name()}", winner


class LudoGame(Game):
    def start_game(self):
        self._status = "Finished"
        winner = random.choice(self._players)
        return f"Ludo Game Over! Winner: {winner.get_name()}", winner


# Match class
class Match:
    _match_counter = 1

    def __init__(self, players, game_type):
        self._match_id = Match._match_counter
        Match._match_counter += 1
        self._players = players
        self._game_type = game_type
        self._winner = None

    def play_match(self):
        if self._game_type.lower() == "chess":
            game = ChessGame(self._match_id, self._players)
        else:
            game = LudoGame(self._match_id, self._players)

        result, self._winner = game.start_game()
        self._winner.update_score(10)
        return result

    def get_results(self):
        return f"Match {self._match_id} Winner: {self._winner.get_name()}"


# GameManager controller
class GameManager:
    def __init__(self):
        self.players = []

    def register_player(self, username, email):
        player = Player(username, email)
        self.players.append(player)
        print(f"Player {username} registered successfully!")

    def show_leaderboard(self):
        print("\nLeaderboard:")
        for p in sorted(self.players, key=lambda x: x.get_score(), reverse=True):
            print(f"{p.get_name()} - {p.get_score()} points")

    def get_player_by_name(self, name):
        for p in self.players:
            if p.get_name() == name:
                return p
        return None


# CLI interface
def main():
    manager = GameManager()

    while True:
        print("\n--- Online Multiplayer Game System ---")
        print("1. Register Player")
        print("2. Create Match")
        print("3. Show Leaderboard")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter username: ")
            email = input("Enter email: ")
            manager.register_player(name, email)

        elif choice == "2":
            p1 = input("Enter Player 1 name: ")
            p2 = input("Enter Player 2 name: ")
            game_type = input("Enter Game Type (Chess/Ludo): ")

            player1 = manager.get_player_by_name(p1)
            player2 = manager.get_player_by_name(p2)

            if player1 and player2:
                match = Match([player1, player2], game_type)
                print(match.play_match())
                print(match.get_results())
            else:
                print("One or both players not found!")

        elif choice == "3":
            manager.show_leaderboard()

        elif choice == "4":
            print("Exiting system...")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
