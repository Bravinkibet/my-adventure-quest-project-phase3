import time
from level import Levels  # Assuming Levels class is defined in level.py

class AdventureQuest:
    def __init__(self, player_name):
        """
        Initializes the AdventureQuest game with the player's name and creates an instance of Levels.
        
        Parameters:
        player_name (str): The name of the player.
        """
        self.player_name = player_name
        self.levels = Levels()
        self.player_id = self.levels.add_player(player_name)

    def start_game(self):
        """
        Starts the AdventureQuest game by welcoming the player and presenting various options.
        """
        print(f"Welcome, {self.player_name}, to Adventure Quest!")
        time.sleep(2)
        print("Your journey begins now...\n")
        time.sleep(2)

        while True:
            print("\nChoose your action:")
            print("1. Play level")
            print("2. View All Players")
            print("3. Update Player Name")
            print("4. Delete Player")
            print("5. Exit game")
            choice = input("Enter the number of your choice: ")

            if choice == "1":
                self.play_level()
            elif choice == "2":
                self.view_all_players()
            elif choice == "3":
                self.update_player_name()
            elif choice == "4":
                self.delete_player()
            elif choice == "5":
                print(f"Thank you for playing Adventure Quest, {self.player_name}! Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid action.\n")

    def play_level(self):
        """
        Presents level options to the player and starts the selected level.
        """
        while True:
            print("\nChoose your level:")
            print("1. Forest")
            print("2. Mountains")
            print("3. Desert")
            print("4. Jungle")
            print("5. Sky")
            print("6. Return to main menu")
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
                print("Returning to main menu...")
                break
            else:
                print("Invalid choice. Please select a valid level.\n")

    def view_all_players(self):
        """
        Displays all players currently registered in the game.
        """
        players = self.levels.get_all_players()
        if players:
            print("\nAll Players:")
            for player in players:
                print(f"ID: {player[0]}, Name: {player[1]}")
        else:
            print("No players found.")

    def update_player_name(self):
        """
        Allows the player to update their name.
        """
        new_name = input("Enter your new name: ")
        self.levels.update_player_name(self.player_id, new_name)
        self.player_name = new_name
        print(f"Player name updated successfully to: {new_name}")

    def delete_player(self):
        """
        Allows the player to delete their profile from the game.
        """
        confirm = input(f"Are you sure you want to delete your profile, {self.player_name}? This action cannot be undone. (yes/no): ").strip().lower()
        if confirm == "yes":
            self.levels.delete_player(self.player_id)
            print(f"Player {self.player_name} deleted successfully. Goodbye!")
            quit()
        else:
            print("Deletion canceled. Returning to main menu.")

if __name__ == "__main__":
    player_name = input("Enter your name: ")
    game = AdventureQuest(player_name)
    game.start_game()
