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
                            player_id INTEGER,
                            environment TEXT,
                            challenge TEXT,
                            choice TEXT,
                            outcome TEXT,
                            FOREIGN KEY(player_id) REFERENCES players(id)
                          )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS players (
                            id INTEGER PRIMARY KEY,
                            name TEXT
                          )''')
        self.conn.commit()

    def add_player(self, name):
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO players (name) VALUES (?)''', (name,))
        self.conn.commit()
        return cursor.lastrowid

    def record_progress(self, player_id, environment, challenge, choice, outcome):
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO game_progress (player_id, environment, challenge, choice, outcome) 
                          VALUES (?, ?, ?, ?, ?)''', (player_id, environment, challenge, choice, outcome))
        self.conn.commit()

    def validate_choice(self, choice, valid_choices):
        return choice in valid_choices

    def prompt_choice(self, message, valid_choices):
        choice = input(message)
        while not self.validate_choice(choice, valid_choices):
            print("Invalid choice. Please select a valid option.")
            choice = input(message)
        return choice

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
        choice = input("Do you want to use your climbing gear (1) or try to find an easier route (2)? ")
        time.sleep(2)
        if choice == "1":
            outcome = "You use your climbing gear to safely navigate the rocky path."
            print(outcome)
            time.sleep(2)
        elif choice == "2":
            outcome = "You search for an easier route and find a safer path, but it takes more time."
            print(outcome)
            time.sleep(2)
        else:
            outcome = "You hesitate too long and have to backtrack to find a new path."
            print(outcome)
            time.sleep(2)
        self.record_progress(player_id, 'Mountains', 'Rocky path', choice, outcome)

        # Challenge 2: Snowstorm
        print("Challenge 2: Snowstorm")
        time.sleep(2)
        print("A sudden snowstorm blows in, reducing visibility to near zero.")
        time.sleep(2)
        choice = input("Do you want to set up camp and wait out the storm (1) or push forward to reach the summit (2)? ")
        time.sleep(2)
        if choice == "1":
            outcome = "You decide to set up camp, using your supplies to create a shelter against the biting wind and snow."
            print(outcome)
            time.sleep(2)
            print("After a long and harsh night, the blizzard subsides, revealing a clear path to the summit.")
            time.sleep(2)
            print("You gather your strength and make the final ascent, reaching the top and enjoying the breathtaking view.")
            time.sleep(2)
        elif choice == "2":
            outcome = "Despite the blizzard, you push forward, determined to reach the summit."
            print(outcome)
            time.sleep(2)
            print("After a grueling struggle, you finally make it to the top, triumphant in your accomplishment.")
            time.sleep(2)
            print("The storm clears, revealing the stunning landscape below.")
            time.sleep(2)
        else:
            outcome = "Your indecision leaves you vulnerable to the elements, and the blizzard takes its toll."
            print(outcome)
            time.sleep(2)
            print("You barely survive the night, but you manage to reach the summit the next day, exhausted but victorious.")
            time.sleep(2)
        self.record_progress(player_id, 'Mountains', 'Snowstorm', choice, outcome)

        print("Congratulations! You have conquered the Mountains and reached the summit!")
        print("Your adventure continues...\n")

    def game_desert(self, player_id):
        self.record_progress(player_id, 'Desert', 'Start', '', 'Player enters the desert')
        print("Welcome to the Desert! The scorching sun beats down as you traverse the endless dunes...")
        time.sleep(2)
        print("As you navigate the harsh landscape, you encounter a series of challenges.")
        time.sleep(2)

        # Challenge 1: Oasis
        print("Challenge 1: Oasis")
        time.sleep(2)
        print("You spot an oasis in the distance, a potential source of water and shade.")
        time.sleep(2)
        choice = input("Do you want to head towards the oasis (1) or continue on your current path (2)? ")
        time.sleep(2)
        if choice == "1":
            outcome = "You head towards the oasis and find much-needed water and rest."
            print(outcome)
            time.sleep(2)
        elif choice == "2":
            outcome = "You continue on your path, conserving your water but maintaining a steady pace."
            print(outcome)
            time.sleep(2)
        else:
            outcome = "You hesitate and lose precious time, but eventually decide to move on."
            print(outcome)
            time.sleep(2)
        self.record_progress(player_id, 'Desert', 'Oasis', choice, outcome)

        # Challenge 2: Sandstorm
        print("Challenge 2: Sandstorm")
        time.sleep(2)
        print("A sudden sandstorm erupts, reducing visibility and making progress difficult.")
        time.sleep(2)
        choice = input("Do you want to find shelter and wait out the storm (1) or keep moving and try to navigate through it (2)? ")
        time.sleep(2)
        if choice == "1":
            outcome = "You find shelter behind a dune, waiting out the storm and avoiding its worst effects."
            print(outcome)
            time.sleep(2)
        elif choice == "2":
            outcome = "You press on through the storm, using your gear to protect yourself from the worst of the sand."
            print(outcome)
            time.sleep(2)
        else:
            outcome = "You hesitate and the storm catches you off guard, but you manage to find shelter just in time."
            print(outcome)
            time.sleep(2)
        self.record_progress(player_id, 'Desert', 'Sandstorm', choice, outcome)

        print("Congratulations! You have survived the Desert and its harsh conditions!")
        print("Your adventure continues...\n")

    def game_jungle(self, player_id):
        self.record_progress(player_id, 'Jungle', 'Start', '', 'Player enters the jungle')
        print("Welcome to the Jungle! The dense foliage surrounds you as you make your way through the undergrowth...")
        time.sleep(2)
        print("As you navigate the lush and vibrant jungle, you encounter a series of challenges.")
        time.sleep(2)

        # Challenge 1: River crossing
        print("Challenge 1: River crossing")
        time.sleep(2)
        print("You come across a wide river with strong currents.")
        time.sleep(2)
        choice = input("Do you want to build a raft (1) or try to swim across (2)? ")
        time.sleep(2)
        if choice == "1":
            outcome = "You build a sturdy raft and manage to cross the river safely."
            print(outcome)
            time.sleep(2)
        elif choice == "2":
            outcome = "You bravely swim across, but the strong currents make it a difficult journey."
            print(outcome)
            time.sleep(2)
        else:
            outcome = "You hesitate and the opportunity to cross easily slips away, but you find another way around."
            print(outcome)
            time.sleep(2)
        self.record_progress(player_id, 'Jungle', 'River crossing', choice, outcome)

        # Challenge 2: Wild animals
        print("Challenge 2: Wild animals")
        time.sleep(2)
        print("You hear rustling in the bushes. Suddenly, a wild animal appears!")
        time.sleep(2)
        choice = input("Do you want to try to scare the animal away (1) or slowly back away and find another route (2)? ")
        time.sleep(2)
        if choice == "1":
            outcome = "You bravely face the animal and manage to scare it away, clearing your path forward."
            print(outcome)
            time.sleep(2)
        elif choice == "2":
            outcome = "You carefully back away and find another route, avoiding the animal."
            print(outcome)
            time.sleep(2)
        else:
            outcome = "Your hesitation puts you in danger, but you manage to escape unharmed."
            print(outcome)
            time.sleep(2)
        self.record_progress(player_id, 'Jungle', 'Wild animals', choice, outcome)

        print("Congratulations! You have survived the Jungle and its wild inhabitants!")
        print("Your adventure continues...\n")

    def game_sky(self, player_id):
        self.record_progress(player_id, 'Sky', 'Start', '', 'Player takes to the skies')
        print("Welcome to the Sky! You soar high above the clouds, navigating through the open air...")
        time.sleep(2)
        print("As you fly through the sky, you encounter a series of challenges.")
        time.sleep(2)

        # Challenge 1: Storm clouds
        print("Challenge 1: Storm clouds")
        time.sleep(2)
        print("Dark storm clouds loom ahead, threatening your safe passage.")
        time.sleep(2)
        choice = input("Do you want to fly around the storm (1) or attempt to fly through it (2)? ")
        time.sleep(2)
        if choice == "1":
            outcome = "You navigate around the storm, avoiding its dangers but adding time to your journey."
            print(outcome)
            time.sleep(2)
        elif choice == "2":
            outcome = "You fly through the storm, facing turbulent winds and lightning, but emerge safely on the other side."
            print(outcome)
            time.sleep(2)
        else:
            outcome = "You hesitate and the storm catches you off guard, but you manage to fly through it with some difficulty."
            print(outcome)
            time.sleep(2)
        self.record_progress(player_id, 'Sky', 'Storm clouds', choice, outcome)

        # Challenge 2: Bird attack
        print("Challenge 2: Bird attack")
        time.sleep(2)
        print("A flock of aggressive birds suddenly appears, threatening your safety.")
        time.sleep(2)
        choice = input("Do you want to try to outmaneuver the birds (1) or use a defensive tool to scare them away (2)? ")
        time.sleep(2)
        if choice == "1":
            outcome = "You skillfully outmaneuver the birds, avoiding their attacks."
            print(outcome)
            time.sleep(2)
        elif choice == "2":
            outcome = "You use a defensive tool to scare away the birds, clearing your path."
            print(outcome)
            time.sleep(2)
        else:
            outcome = "Your hesitation leaves you vulnerable, but you manage to escape the birds with minor injuries."
            print(outcome)
            time.sleep(2)
        self.record_progress(player_id, 'Sky', 'Bird attack', choice, outcome)

        print("Congratulations! You have navigated the Sky and its aerial challenges!")
        print("Your adventure continues...\n")