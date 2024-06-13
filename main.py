import time
from level import Levels

class AdventureQuest:
    def __init__(self, player_name):
        """
        Initializes the AdventureQuest game with the player's name and creates an instance of Levels.
        """
        self.player_name = player_name
        self.levels = Levels()
        self.player_id = self.levels.add_player(player_name)

    def start_game(self):
        """
        Starts the AdventureQuest game by welcoming the player and presenting level options.
        """
        print(f"Welcome, {self.player_name}, to Adventure Quest!")
        time.sleep(2)
        print("Your journey begins now...\n")
        time.sleep(2)

        while True:
            print("Choose your level:")
            print("1. Forest")
            print("2. Mountains")
            print("3. Desert")
            print("4. Jungle")
            print("5. Sky")
            print("6. Exit game")
            choice = input("Enter the number of your choice: ")

            if choice == "1":
                self.levels.game_forest(self.player_id)
            elif choice == "2":
                self.levels.game_mountains(self.player_id)
            elif choice == "3":
                self.levels.game_desert(self.player_id)
            elif choice == "4":
                self.levels.game_jungle(self.player_id)
            elif choice == "5":
                self.levels.game_sky(self.player_id)
            elif choice == "6":
                print("Thank you for playing Adventure Quest! Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid level.\n")

if __name__ == "__main__":
    player_name = input("Enter your name: ")
    game = AdventureQuest(player_name)
    game.start_game()
