import sqlite3
import time

class Levels:
    def __init__(self):
        self.conn = sqlite3.connect('game_data.db')
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS game_progress (
                            id INTEGER PRIMARY KEY,
                            environment TEXT,
                            challenge TEXT,
                            choice TEXT,
                            outcome TEXT
                          )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS players (
                            id INTEGER PRIMARY KEY,
                            name TEXT
                          )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS game_player_progress (
                            id INTEGER PRIMARY KEY,
                            player_id INTEGER,
                            progress_id INTEGER,
                            FOREIGN KEY(player_id) REFERENCES players(id),
                            FOREIGN KEY(progress_id) REFERENCES game_progress(id)
                          )''')
        self.conn.commit()

    def add_player(self, name):
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO players (name) VALUES (?)''', (name,))
        self.conn.commit()
        return cursor.lastrowid

    def get_player_by_id(self, player_id):
        cursor = self.conn.cursor()
        cursor.execute('''SELECT * FROM players WHERE id = ?''', (player_id,))
        return cursor.fetchone()

    def update_player_name(self, player_id, new_name):
        cursor = self.conn.cursor()
        cursor.execute('''UPDATE players SET name = ? WHERE id = ?''', (new_name, player_id))
        self.conn.commit()

    def delete_player(self, player_id):
        cursor = self.conn.cursor()
        cursor.execute('''DELETE FROM players WHERE id = ?''', (player_id,))
        self.conn.commit()

    def record_progress(self, player_id, environment, challenge, choice, outcome):
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO game_progress (environment, challenge, choice, outcome) 
                          VALUES (?, ?, ?, ?)''', (environment, challenge, choice, outcome))
        progress_id = cursor.lastrowid
        cursor.execute('''INSERT INTO game_player_progress (player_id, progress_id) 
                          VALUES (?, ?)''', (player_id, progress_id))
        self.conn.commit()

    def validate_choice(self, choice, valid_choices):
        return choice in valid_choices

    def prompt_choice(self, message, valid_choices):
        choice = input(message)
        while not self.validate_choice(choice, valid_choices):
            print("Invalid choice. Please select a valid option.")
            choice = input(message)
        return choice

    def start_game(self):
        while True:
            print("\nChoose your action:")
            print("1. Play level")
            print("2. View All Players")
            print("3. Update Player Name")
            print("4. Delete Player")
            print("5. Exit game")
            choice = self.prompt_choice("Enter the number of your choice: ", ['1', '2', '3', '4', '5'])

            if choice == '1':
                self.play_level()
            elif choice == '2':
                self.view_all_players()
            elif choice == '3':
                self.update_player_menu()
            elif choice == '4':
                self.delete_player_menu()
            elif choice == '5':
                print("Exiting game. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def view_all_players(self):
        cursor = self.conn.cursor()
        cursor.execute('''SELECT * FROM players''')
        players = cursor.fetchall()
        if players:
            print("\nAll Players:")
            for player in players:
                print(f"ID: {player[0]}, Name: {player[1]}")
        else:
            print("No players found.")

    def update_player_menu(self):
        print("\nUpdate Player Name:")
        player_id = input("Enter the ID of the player you want to update: ")
        player = self.get_player_by_id(player_id)
        if player:
            new_name = input(f"Enter the new name for {player[1]}: ")
            self.update_player_name(player_id, new_name)
            print(f"Player name updated successfully.")
        else:
            print(f"Player with ID {player_id} not found.")

    def delete_player_menu(self):
        print("\nDelete Player:")
        player_id = input("Enter the ID of the player you want to delete: ")
        player = self.get_player_by_id(player_id)
        if player:
            confirm = input(f"Are you sure you want to delete {player[1]}? (yes/no): ").strip().lower()
            if confirm == "yes":
                self.delete_player(player_id)
                print(f"Player {player[1]} deleted successfully.")
            else:
                print(f"Deletion of player {player[1]} canceled.")
        else:
            print(f"Player with ID {player_id} not found.")

    def play_level(self):
        player_id = input("Enter your player ID to start playing: ")
        print("Choose your level:")
        print("1. Forest")
        print("2. Mountains")
        print("3. Desert")
        print("4. Jungle")
        print("5. Sky")
        choice = self.prompt_choice("Enter the number of your choice: ", ['1', '2', '3', '4', '5'])
        
        if choice == '1':
            self.game_forest(player_id)
        elif choice == '2':
            self.game_mountains(player_id)
        elif choice == '3':
            self.game_desert(player_id)
        elif choice == '4':
            self.game_jungle(player_id)
        elif choice == '5':
            self.game_sky(player_id)
        else:
            print("Invalid choice. Please select a valid option.")
    
    def game_forest(self, player_id):
        self.record_progress(player_id, 'Forest', 'Start', '', 'Player enters the forest')
        print("Welcome to the Forest! The trees tower above you as you begin your journey...")
        time.sleep(2)
        print("As you navigate the dense undergrowth, you encounter a series of challenges.")
        time.sleep(2)
        
        # Challenge 1: Finding a path
        print("Challenge 1: Finding a path")
        time.sleep(2)
        print("You come across a fork in the path. One direction looks well-traveled, while the other is overgrown and mysterious.")
        time.sleep(2)
        choice = self.prompt_choice("Do you want to take the well-traveled path (1) or the mysterious path (2)? ", ['1', '2'])
        outcome = "You take the well-traveled path and make steady progress through the forest." if choice == "1" else "You choose the mysterious path and encounter hidden dangers, but also hidden treasures."
        print(outcome)
        time.sleep(2)
        self.record_progress(player_id, 'Forest', 'Finding a path', choice, outcome)

        # Challenge 2: Wild animals
        print("Challenge 2: Wild animals")
        time.sleep(2)
        print("You hear rustling in the bushes. Suddenly, a wild animal appears!")
        time.sleep(2)
        choice = self.prompt_choice("Do you want to try to scare the animal away (1) or slowly back away and find another route (2)? ", ['1', '2'])
        outcome = "You bravely face the animal and manage to scare it away, clearing your path forward." if choice == "1" else "You carefully back away and find another route, avoiding the animal."
        print(outcome)
        time.sleep(2)
        self.record_progress(player_id, 'Forest', 'Wild animals', choice, outcome)

        # Challenge 3: Crossing a river
        print("Challenge 3: Crossing a river")
        time.sleep(2)
        print("You come across a fast-flowing river. There's a rickety bridge and a narrow, slippery log.")
        time.sleep(2)
        choice = self.prompt_choice("Do you want to cross using the bridge (1) or the log (2)? ", ['1', '2'])
        outcome = "You carefully cross the bridge, despite its creaking protests." if choice == "1" else "You balance your way across the log, narrowly avoiding a fall into the river."
        print(outcome)
        time.sleep(2)
        self.record_progress(player_id, 'Forest', 'Crossing a river', choice, outcome)

        # Final Challenge: Forest clearing
        print("Final Challenge: Forest clearing")
        time.sleep(2)
        print("You reach a clearing with a mysterious glowing tree in the center.")
        time.sleep(2)
        print("The tree seems to beckon you, but you sense potential danger.")
        time.sleep(2)
        choice = self.prompt_choice("Do you want to approach the tree (1) or avoid it and continue your journey (2)? ", ['1', '2'])
        outcome = "You approach the tree and discover it's a source of magical energy, granting you a boon for your journey." if choice == "1" else "You wisely avoid the tree, continuing your journey with caution."
        print(outcome)
        time.sleep(2)
        self.record_progress(player_id, 'Forest', 'Forest clearing', choice, outcome)

        print("Congratulations! You have conquered the Forest and braved its many challenges!")
        print("Your adventure continues...\n")
    def game_mountains(self, player_id):
        self.record_progress(player_id, 'Mountains', 'Start', '', 'Player begins the ascent')
        print("Welcome to the Mountains! The air is crisp and the path is steep as you begin your ascent...")
        time.sleep(2)
        print("As you climb higher, you encounter a series of challenges.")
        time.sleep(2)

        # Challenge 1: Rocky path
        print("Challenge 1: Rocky path")
        time.sleep(2)
        print("The path becomes rocky and treacherous. You need to choose your steps carefully.")
        time.sleep(2)
        choice = self.prompt_choice("Do you want to use your climbing gear (1) or try to find an easier route (2)? ", ['1', '2'])
        outcome = "You use your climbing gear to safely navigate the rocky path." if choice == "1" else "You search for an easier route and find a safer path, but it takes more time."
        print(outcome)
        time.sleep(2)
        self.record_progress(player_id, 'Mountains', 'Rocky path', choice, outcome)

        # Challenge 2: Snowstorm
        print("Challenge 2: Snowstorm")
        time.sleep(2)
        print("A sudden snowstorm blows in, reducing visibility to near zero.")
        time.sleep(2)
        choice = self.prompt_choice("Do you want to set up camp and wait out the storm (1) or push forward to reach the summit (2)? ", ['1', '2'])
        outcome = "You decide to set up camp, using your supplies to create a shelter against the biting wind and snow." if choice == "1" else "Despite the blizzard, you push forward, determined to reach the summit."
        print(outcome)
        time.sleep(2)
        self.record_progress(player_id, 'Mountains', 'Snowstorm', choice, outcome)

        # Challenge 3: Summit Climb
        print("Challenge 3: Summit Climb")
        time.sleep(2)
        print("You reach the final stretch towards the summit. The air thins as you climb higher.")
        time.sleep(2)
        choice = self.prompt_choice("Do you want to take a break and acclimatize (1) or push through the fatigue to reach the summit (2)? ", ['1', '2'])
        outcome = "You take a break to acclimatize, ensuring your body adjusts to the altitude." if choice == "1" else "You push through the fatigue and successfully reach the summit, taking in the breathtaking view."
        print(outcome)
        time.sleep(2)
        self.record_progress(player_id, 'Mountains', 'Summit Climb', choice, outcome)

        print("Congratulations! You have conquered the Mountains and reached the summit!")
        print("Your adventure continues...\n")
