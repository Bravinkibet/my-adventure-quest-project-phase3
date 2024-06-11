from game import AdventureQuest

def main():
    player_name = input("Welcome to AdventureQuest! Please enter your name: ")
    game = AdventureQuest(player_name)
    game.start_game()

if __name__ == "__main__":
    main()
