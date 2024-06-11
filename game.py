import time

class AdventureQuest:
    def __init__(self, player_name):
        self.player_name = player_name
        self.levels = {
            1: ["Forest"],
            2: ["Mountains"],
            3: ["Desert"],
            4: ["Jungle"],
            5: ["Sky"]
        }
        self.current_level = 1

    def start_game(self):
        print(f"Welcome, {self.player_name}, to the AdventureQuest game!")
        print("Your journey begins now!")
        self.play_level()

    def play_level(self):
        print(f"You are now at Level {self.current_level}")
        game = self.levels[self.current_level][0]
        print(f"Game: {game}")
        self.play_game(game)
        self.current_level += 1
        if self.current_level <= len(self.levels):
            choice = input("Congratulations Do you want to proceed to the next level? (yes/no): ")
            if choice.lower() == "yes":
                self.play_level()
            else:
                print("Thanks for playing AdventureQuest!")

    def play_game(self, game):
        if game == "Forest":
            self.game_forest()
        elif game == "Mountains":
            self.game_mountains()
        elif game == "Desert":
            self.game_desert()
        elif game == "Jungle":
            self.game_jungle()
        elif game == "Sky":
            self.game_sky()

    def game_forest(self):
        print("Welcome to the Forest You find yourself surrounded by ancient trees and mysterious creatures...")
        time.sleep(2)
        print("As you venture deeper into the forest, you encounter a pack of wolves blocking your path.")
        time.sleep(2)
        print("You must decide whether to confront the wolves or find an alternate route.")
        choice = input("What will you do? (confront/flee): ").lower()
        
        if choice == "confront":
            print(f"\nYou bravely face the wolves, brandishing your weapon.\n")
            time.sleep(2)
            print("After a fierce battle, the wolves retreat, allowing you to continue your journey.")
            time.sleep(2)
            print("But beware, more challenges lie ahead...\n")
            
            # New character interaction
            print("Suddenly, you hear a rustling behind you. Turning around, you see an old hermit standing there.")
            time.sleep(2)
            print("The hermit says, 'I've been watching you. The forest has many secrets. One leads to a powerful artifact.'")
            time.sleep(2)
            print("Do you wish to learn about this artifact?")
            decision = input("Yes/No: ").lower()
            
            if decision == "yes":
                print("\nThe hermit tells you about a legendary artifact known as the 'Heart of the Forest', said to grant immense power to its possessor.")
                time.sleep(2)
                print("He warns you that the path to the Heart is fraught with danger and that only the pure of heart may claim it.")
                time.sleep(2)
                print("Would you like to embark on this quest?")
                quest_decision = input("Embark on the quest/Return to the main path: ").lower()
                
                if quest_decision == "embark on the quest":
                    print("\nYou set off on the quest for the Heart of the Forest, facing numerous trials along the way.")
                    time.sleep(2)
                    print("This is just the beginning of your adventure in the Forest...\n")
                else:
                    print("\nDeciding against the quest, you continue on your original path, leaving the hermit behind.")
                    time.sleep(2)
                    print("Your adventure continues...\n")
            else:
                print("\nChoosing not to learn about the artifact, you continue on your journey, leaving the hermit behind.")
                time.sleep(2)
                print("Your adventure continues...\n")
        elif choice == "flee":
            print("\nYou choose to flee from the wolves, seeking safety in the dense undergrowth.")
            time.sleep(2)
            print("As you run, you stumble upon a hidden cave.")
            time.sleep(2)
            print("Inside the cave, you find a valuable treasure, guarded by a fearsome dragon.")
            time.sleep(2)
            print("You must decide whether to face the dragon or retreat from the cave.")
            choice = input("What will you do? (face/retreat): ").lower()
            
            if choice == "face":
                print("\nYou summon your courage and prepare to confront the dragon head-on.")
                time.sleep(2)
                print("After a grueling battle, you emerge victorious, claiming the treasure as your own.")
                time.sleep(2)
                print("Congratulations You have conquered the Forest and obtained the treasure.")
            elif choice == "retreat":
                print("\nYou wisely choose to retreat from the cave, avoiding a potentially deadly encounter.")
                time.sleep(2)
                print("As you leave the forest, you vow to return one day and face the dragon.")
                time.sleep(2)
                print("Your adventure in the Forest comes to an end...\n")
        else:
            print("\nInvalid choice. Please try again.")


def game_mountains(self):
    print("Welcome to the Mountains! The rugged peaks loom overhead, challenging you to climb higher...")
    time.sleep(2)
    print("As you trek through the rocky terrain, you encounter a series of obstacles and challenges.")
    time.sleep(2)
    
    # Obstacle 1: Cliffside Path
    print("Obstacle 1: Cliffside Path")
    time.sleep(2)
    print("You come across a narrow path along the edge of a steep cliff. It looks perilous.")
    time.sleep(2)
    choice = input("Do you want to risk taking the cliffside path (1) or find an alternative route (2)? ")
    time.sleep(2)
    if choice == "1":
        print("You carefully navigate the cliffside path, clinging to the rock face as you move forward.")
        time.sleep(2)
        print("After a tense journey, you successfully make it across the cliffside.")
        time.sleep(2)
    elif choice == "2":
        print("You search for a safer route and eventually find a winding path leading up the mountain.")
        time.sleep(2)
        print("Although it takes longer, you avoid the dangerous cliffside and continue your ascent.")
        time.sleep(2)
    else:
        print("You hesitate too long and lose your footing, slipping off the cliffside!")
        time.sleep(2)
        print("Luckily, you manage to grab onto a ledge and pull yourself to safety.")
        time.sleep(2)
    
    # Obstacle 2: Mountain Pass
    print("Obstacle 2: Mountain Pass")
    time.sleep(2)
    print("As you climb higher, you reach a narrow mountain pass blocked by a large boulder.")
    time.sleep(2)
    choice = input("Do you want to try to move the boulder (1) or find a way around it (2)? ")
    time.sleep(2)
    if choice == "1":
        print("You put all your strength into pushing the boulder, slowly inching it out of the way.")
        time.sleep(2)
        print("With a final effort, you manage to clear the path and continue on your journey.")
        time.sleep(2)
    elif choice == "2":
        print("You explore the surrounding area and discover a hidden trail leading around the boulder.")
        time.sleep(2)
        print("It's a longer route, but you avoid the risk of getting trapped by the boulder.")
        time.sleep(2)
    else:
        print("You freeze in indecision, and a sudden gust of wind causes the boulder to tumble down the mountain!")
        time.sleep(2)
        print("You narrowly dodge the rolling boulder and quickly find another path to safety.")
        time.sleep(2)

    # Obstacle 3: Avalanche
    print("Obstacle 3: Avalanche")
    time.sleep(2)
    print("Suddenly, you hear a rumbling noise from above as a cascade of snow and ice comes crashing down.")
    time.sleep(2)
    choice = input("Do you want to try to outrun the avalanche (1) or seek shelter behind a rock (2)? ")
    time.sleep(2)
    if choice == "1":
        print("You sprint as fast as you can, dodging falling debris and leaping over obstacles in your path.")
        time.sleep(2)
        print("With adrenaline coursing through your veins, you narrowly escape the avalanche.")
        time.sleep(2)
    elif choice == "2":
        print("You quickly duck behind a large rock, using it as a shield against the onslaught of snow and ice.")
        time.sleep(2)
        print("The avalanche passes by, leaving you unscathed but shaken by the close call.")
        time.sleep(2)
    else:
        print("You hesitate for too long and are caught in the path of the avalanche!")
        time.sleep(2)
        print("You're swept away by the force of the avalanche, tumbling down the mountain slope.")
        time.sleep(2)

    # Final Challenge: Summit
    print("Final Challenge: Summit")
    time.sleep(2)
    print("After overcoming numerous obstacles, you finally reach the summit of the mountain.")
    time.sleep(2)
    print("However, the journey is not over yet. A fierce blizzard suddenly engulfs the peak, obscuring your vision.")
    time.sleep(2)
    choice = input("Do you want to press on through the blizzard (1) or seek shelter (2)? ")
    time.sleep(2)
    if choice == "1":
        print("You steel yourself against the biting cold and forge ahead, determined to reach your goal.")
        time.sleep(2)
        print("Despite the harsh conditions, you push through the blizzard and emerge victorious at the summit.")
        time.sleep(2)
    elif choice == "2":
        print("You wisely decide to seek shelter from the storm, finding refuge in a nearby cave.")
        time.sleep(2)
        print("After waiting out the blizzard, you emerge from the cave and bask in the glory of your achievement.")
        time.sleep(2)
    else:
        print("Your hesitation costs you precious time, and the blizzard worsens, threatening to overwhelm you.")
        time.sleep(2)
        print("In a last-ditch effort, you brave the storm and push forward, narrowly avoiding disaster.")
        time.sleep(2)

    # Add more game logic here to make the level last at least 10 minutes



def game_desert(self):
    print("Welcome to the Desert! The scorching sun beats down on the arid landscape...")
    time.sleep(2)
    print("As you traverse the endless sands, you encounter a series of challenges and trials.")
    time.sleep(2)
    
    # Challenge 1: Sandstorm
    print("Challenge 1: Sandstorm")
    time.sleep(2)
    print("A fierce sandstorm engulfs the desert, reducing visibility to almost zero.")
    time.sleep(2)
    choice = input("Do you want to try to navigate through the sandstorm (1) or seek shelter (2)? ")
    time.sleep(2)
    if choice == "1":
        print("You forge ahead, relying on your instincts to guide you through the swirling sands.")
        time.sleep(2)
        print("Despite the harsh conditions, you manage to push through the sandstorm and emerge on the other side.")
        time.sleep(2)
    elif choice == "2":
        print("You hunker down behind a large rock, using it as a shield against the raging sandstorm.")
        time.sleep(2)
        print("After waiting out the worst of the storm, you emerge from your makeshift shelter unscathed.")
        time.sleep(2)
    else:
        print("Your indecision leaves you vulnerable to the elements, and you're buffeted by the raging sandstorm.")
        time.sleep(2)
        print("Bruised and battered, you eventually find your way out of the storm, determined to continue your journey.")
        time.sleep(2)

    # Challenge 2: Oasis
    print("Challenge 2: Oasis")
    time.sleep(2)
    print("Amidst the barren desert, you stumble upon a lush oasis teeming with life.")
    time.sleep(2)
    choice = input("Do you want to rest and replenish your supplies at the oasis (1) or continue your journey (2)? ")
    time.sleep(2)
    if choice == "1":
        print("You take a much-needed break, quenching your thirst and refilling your canteen with fresh water.")
        time.sleep(2)
        print("Feeling rejuvenated, you set off once again, grateful for the oasis's respite.")
        time.sleep(2)
    elif choice == "2":
        print("You decide to press on, wary of spending too much time in the oasis and risking dehydration.")
        time.sleep(2)
        print("With renewed determination, you continue your trek across the unforgiving desert.")
        time.sleep(2)
    else:
        print("Your hesitation costs you valuable time, and you miss the opportunity to replenish your supplies.")
        time.sleep(2)
        print("Despite your fatigue, you press on, hoping to find another source of water before it's too late.")
        time.sleep(2)

    # Challenge 3: Sand Dunes
    print("Challenge 3: Sand Dunes")
    time.sleep(2)
    print("You encounter a vast expanse of towering sand dunes, stretching as far as the eye can see.")
    time.sleep(2)
    choice = input("Do you want to attempt to traverse the sand dunes (1) or find a way around them (2)? ")
    time.sleep(2)
    if choice == "1":
        print("You summon all your strength and courage, climbing up and over the towering sand dunes.")
        time.sleep(2)
        print("After a grueling ascent, you finally reach the other side, exhausted but triumphant.")
        time.sleep(2)
    elif choice == "2":
        print("You search for a path around the sand dunes, eventually finding a winding trail leading through a canyon.")
        time.sleep(2)
        print("Although it takes longer, you avoid the treacherous sand dunes and continue your journey.")
        time.sleep(2)
    else:
        print("Your hesitation leaves you stranded in the desert, unsure of which direction to take.")
        time.sleep(2)
        print("After wandering aimlessly for hours, you finally find your way around the sand dunes and continue your quest.")
        time.sleep(2)

    # Final Challenge: Mirage
    print("Final Challenge: Mirage")
    time.sleep(2)
    print("As you near the end of the desert, you're tantalized by the sight of a shimmering oasis in the distance.")
    time.sleep(2)
    choice = input("Do you want to investigate the mirage (1) or continue on your current path (2)? ")
    time.sleep(2)
    if choice == "1":
        print("You follow the mirage, hoping to find water and relief from the oppressive heat.")
        time.sleep(2)
        print("However, as you draw closer, the mirage evaporates before your eyes, leaving you disheartened.")
        time.sleep(2)
    elif choice == "2":
        print("You wisely ignore the mirage and press on, knowing that it's merely a trick of the desert.")
        time.sleep(2)
        print("With determination and perseverance, you finally emerge from the desert, victorious in your quest.")
        time.sleep(2)
    else:
        print("Your curiosity gets the better of you, and you veer off course in pursuit of the mirage.")
        time.sleep(2)
        print("Hours later, you find yourself lost and disoriented, regretting your impulsive decision.")
        time.sleep(2)

    # Add more game logic here to make the level last at least 10 minutes


    import time
import random

def game_jungle(self):
    print("Welcome to the Jungle! The dense foliage surrounds you, obscuring your vision.")
    time.sleep(2)
    print("You hear the sounds of exotic birds and wild animals echoing through the trees.")
    time.sleep(2)
    print("As you journey deeper into the jungle, you encounter a series of challenges and obstacles.")
    time.sleep(2)

    # Challenge 1: River Crossing
    print("Challenge 1: River Crossing")
    time.sleep(2)
    print("You come across a fast-flowing river blocking your path.")
    time.sleep(2)
    choice = input("Do you want to attempt to ford the river (1) or search for a bridge (2)? ")
    time.sleep(2)
    if choice == "1":
        print("You wade into the river, struggling against the strong current.")
        time.sleep(2)
        print("Despite your efforts, you're swept downstream and must find another way across.")
        time.sleep(2)
    elif choice == "2":
        print("You search the jungle for a bridge, eventually finding a sturdy vine spanning the river.")
        time.sleep(2)
        print("With careful footing, you cross the river safely and continue your journey.")
        time.sleep(2)

    # Challenge 2: Hidden Temple
    print("Challenge 2: Hidden Temple")
    time.sleep(2)
    print("While exploring the jungle, you stumble upon a hidden temple buried beneath the foliage.")
    time.sleep(2)
    choice = input("Do you want to enter the temple (1) or continue on your current path (2)? ")
    time.sleep(2)
    if choice == "1":
        print("You enter the temple, marveling at its ancient architecture and intricate carvings.")
        time.sleep(2)
        print("Inside, you discover hidden chambers filled with valuable treasures and artifacts.")
        time.sleep(2)
    elif choice == "2":
        print("You decide to continue your journey through the jungle, leaving the temple unexplored.")
        time.sleep(2)

    # Challenge 3: Tribal Encounter
    print("Challenge 3: Tribal Encounter")
    time.sleep(2)
    print("As you venture deeper into the jungle, you encounter a tribe of indigenous people.")
    time.sleep(2)
    choice = input("Do you want to approach the tribe peacefully (1) or sneak past them unnoticed (2)? ")
    time.sleep(2)
    if choice == "1":
        print("You approach the tribe with caution, offering them gifts as a sign of goodwill.")
        time.sleep(2)
        print("The tribe welcomes you warmly and shares their knowledge of the jungle with you.")
        time.sleep(2)
    elif choice == "2":
        print("You attempt to sneak past the tribe, but they spot you and give chase through the jungle.")
        time.sleep(2)
        print("After a tense pursuit, you manage to evade capture and continue on your way.")
        time.sleep(2)

    # Challenge 4: Lost in the Jungle
    print("Challenge 4: Lost in the Jungle")
    time.sleep(2)
    print("While navigating the dense undergrowth, you lose your sense of direction and become disoriented.")
    time.sleep(2)
    print("You must rely on your instincts to find your way out of the jungle before it's too late.")
    time.sleep(2)
    print("Try to find clues in your surroundings to guide you.")
    time.sleep(2)

    # Generate a random number (1 or 2) to simulate searching for clues
    random.seed()
    clue_search = random.randint(1, 2)
    time.sleep(2)
    if clue_search == 1:
        print("You search for clues and spot a trail of broken branches leading in a certain direction.")
        time.sleep(2)
        print("Following the trail, you eventually emerge from the jungle, relieved to be back on track.")
        time.sleep(2)
    else:
        print("You search for clues but find nothing useful, only adding to your sense of frustration.")
        time.sleep(2)
        print("After what feels like hours of wandering, you stumble upon a familiar landmark and regain your bearings.")
        time.sleep(2)

    # Add more game logic here to make the level last at least 7 minutes

    import time
import random

def game_sky(self):
    print("Welcome to the Sky! You find yourself soaring high above the clouds, surrounded by endless blue.")
    time.sleep(2)
    print("As you glide through the sky, you encounter various challenges and wonders.")
    time.sleep(2)

    # Challenge 1: Cloud Crossing
    print("Challenge 1: Cloud Crossing")
    time.sleep(2)
    print("You come across a vast expanse of clouds blocking your path.")
    time.sleep(2)
    choice = input("Do you want to fly through the clouds (1) or navigate around them (2)? ")
    time.sleep(2)
    if choice == "1":
        print("You dive into the clouds, weaving your way through them with precision and skill.")
        time.sleep(2)
        print("After a thrilling flight, you emerge on the other side unscathed.")
        time.sleep(2)
    elif choice == "2":
        print("You decide to take a detour, skirting around the clouds to avoid any potential hazards.")
        time.sleep(2)
        print("While the journey takes longer, you reach your destination safely.")
        time.sleep(2)

    # Challenge 2: Sky Fortress
    print("Challenge 2: Sky Fortress")
    time.sleep(2)
    print("You spot a massive fortress floating in the sky, bristling with cannons and defenses.")
    time.sleep(2)
    choice = input("Do you want to approach the fortress (1) or steer clear of it (2)? ")
    time.sleep(2)
    if choice == "1":
        print("You fly closer to the fortress, prepared to face whatever challenges lie ahead.")
        time.sleep(2)
        print("As you draw near, you're greeted by a hail of cannon fire from the fortress.")
        time.sleep(2)
        print("You must use all your agility and reflexes to dodge the incoming attacks.")
        time.sleep(2)
        # Add more game logic for the Sky Fortress encounter
    elif choice == "2":
        print("You decide to avoid the fortress, not wanting to risk a confrontation.")
        time.sleep(2)
        print("You continue your journey through the sky, keeping a wary eye on the fortress from a distance.")
        time.sleep(2)

    # Challenge 3: Celestial Puzzle
    print("Challenge 3: Celestial Puzzle")
    time.sleep(2)
    print("You encounter a series of floating platforms arranged in a complex pattern.")
    time.sleep(2)
    choice = input("Do you want to attempt to solve the puzzle (1) or find an alternate route (2)? ")
    time.sleep(2)
    if choice == "1":
        print("You carefully study the pattern of the platforms, searching for a solution.")
        time.sleep(2)
        print("After several attempts, you manage to decipher the pattern and navigate through the puzzle.")
        time.sleep(2)
    elif choice == "2":
        print("You decide to look for another way around the puzzle, not wanting to waste time.")
        time.sleep(2)
        print("After some searching, you find a hidden passage that bypasses the puzzle entirely.")
        time.sleep(2)

    # Add more game logic here to make the level last at least 7 minutes


# Example usage
if __name__ == "__main__":
    game = AdventureQuest(input("Enter your name: "))
    game.start_game()
