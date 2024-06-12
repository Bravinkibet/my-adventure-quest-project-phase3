import time

class Levels:
    def validate_choice(self, choice, valid_choices):
        """
        Validate user input choice against a list of valid choices.
        """
        if choice not in valid_choices:
            print("Invalid choice. Please select a valid option.")
            return False
        return True
    def game_forest(self):
        print("Welcome to the Forest! The trees tower above you as you begin your journey...")
        time.sleep(2)
        print("As you navigate the dense undergrowth, you encounter a series of challenges.")
        time.sleep(2)
        
        # Challenge 1: Finding a path
        print("Challenge 1: Finding a path")
        time.sleep(2)
        print("You come across a fork in the path. One direction looks well-traveled, while the other is overgrown and mysterious.")
        time.sleep(2)
        choice = input("Do you want to take the well-traveled path (1) or the mysterious path (2)? ")
        time.sleep(2)
        if choice == "1":
            print("You take the well-traveled path and make steady progress through the forest.")
            time.sleep(2)
        elif choice == "2":
            print("You choose the mysterious path and encounter hidden dangers, but also hidden treasures.")
            time.sleep(2)
        else:
            print("You hesitate too long and lose your way, forcing you to find a new path.")
            time.sleep(2)

        # Challenge 2: Wild animals
        print("Challenge 2: Wild animals")
        time.sleep(2)
        print("You hear rustling in the bushes. Suddenly, a wild animal appears!")
        time.sleep(2)
        choice = input("Do you want to try to scare the animal away (1) or slowly back away and find another route (2)? ")
        time.sleep(2)
        if choice == "1":
            print("You bravely face the animal and manage to scare it away, clearing your path forward.")
            time.sleep(2)
        elif choice == "2":
            print("You carefully back away and find another route, avoiding the animal.")
            time.sleep(2)
        else:
            print("Your hesitation puts you in danger, but you manage to escape unharmed.")
            time.sleep(2)

        # Challenge 3: Crossing a river
        print("Challenge 3: Crossing a river")
        time.sleep(2)
        print("You come across a fast-flowing river. There's a rickety bridge and a narrow, slippery log.")
        time.sleep(2)
        choice = input("Do you want to cross using the bridge (1) or the log (2)? ")
        time.sleep(2)
        if choice == "1":
            print("You carefully cross the bridge, despite its creaking protests.")
            time.sleep(2)
        elif choice == "2":
            print("You balance your way across the log, narrowly avoiding a fall into the river.")
            time.sleep(2)
        else:
            print("You hesitate too long and have to find a new way across, costing you precious time.")
            time.sleep(2)

        # Final Challenge: Forest clearing
        print("Final Challenge: Forest clearing")
        time.sleep(2)
        print("You reach a clearing with a mysterious glowing tree in the center.")
        time.sleep(2)
        print("The tree seems to beckon you, but you sense potential danger.")
        time.sleep(2)
        choice = input("Do you want to approach the tree (1) or avoid it and continue your journey (2)? ")
        time.sleep(2)
        if choice == "1":
            print("You approach the tree and discover it's a source of magical energy, granting you a boon for your journey.")
            time.sleep(2)
        elif choice == "2":
            print("You wisely avoid the tree, continuing your journey with caution.")
            time.sleep(2)
        else:
            print("You hesitate too long, and the opportunity passes as the tree's glow fades.")
            time.sleep(2)

        print("Congratulations! You have conquered the Forest and braved its many challenges!")
        print("Your adventure continues...\n")

    def game_mountains(self):
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
            print("You use your climbing gear to safely navigate the rocky path.")
            time.sleep(2)
        elif choice == "2":
            print("You search for an easier route and find a safer path, but it takes more time.")
            time.sleep(2)
        else:
            print("You hesitate too long and have to backtrack to find a new path.")
            time.sleep(2)

        # Challenge 2: Snowstorm
        print("Challenge 2: Snowstorm")
        time.sleep(2)
        print("A sudden snowstorm blows in, reducing visibility to near zero.")
        time.sleep(2)
        choice = input("Do you want to set up camp and wait out the storm (1) or push forward to reach the summit (2)? ")
        time.sleep(2)
        if choice == "1":
            print("You decide to set up camp, using your supplies to create a shelter against the biting wind and snow.")
            time.sleep(2)
            print("After a long and harsh night, the blizzard subsides, revealing a clear path to the summit.")
            time.sleep(2)
            print("You gather your strength and make the final ascent, reaching the top and enjoying the breathtaking view.")
            time.sleep(2)
        elif choice == "2":
            print("Despite the blizzard, you push forward, determined to reach the summit.")
            time.sleep(2)
            print("After a grueling struggle, you finally make it to the top, triumphant in your accomplishment.")
            time.sleep(2)
            print("The storm clears, revealing the stunning landscape below.")
            time.sleep(2)
        else:
            print("Your indecision leaves you vulnerable to the elements, and the blizzard takes its toll.")
            time.sleep(2)
            print("You barely survive the night, but you manage to reach the summit the next day, exhausted but victorious.")
            time.sleep(2)

        print("Congratulations! You have conquered the Mountains and reached the summit!")
        print("Your adventure continues...\n")

    def game_desert(self):
        print("Welcome to the Desert! The scorching sun beats down as you traverse the endless dunes...")
        time.sleep(2)
        print("As you navigate the harsh environment, you encounter a series of challenges.")
        time.sleep(2)
        
        # Challenge 1: Oasis
        print("Challenge 1: Oasis")
        time.sleep(2)
        print("You come across an oasis, a rare sight in the desert. It offers a chance to rest and replenish your water supply.")
        time.sleep(2)
        choice = input("Do you want to stop and rest at the oasis (1) or continue your journey without stopping (2)? ")
        time.sleep(2)
        if choice == "1":
            print("You take a break at the oasis, enjoying the cool shade and refreshing water.")
            time.sleep(2)
            print("After resting, you feel rejuvenated and ready to continue your journey.")
            time.sleep(2)
        elif choice == "2":
            print("You decide to press on, determined to reach your destination without delay.")
            time.sleep(2)
            print("Although you miss the chance to rest, you make good progress in your journey.")
            time.sleep(2)
        else:
            print("You hesitate for too long, and the oasis fades away, revealing it to be a mirage!")
            time.sleep(2)
            print("You continue your journey, now more cautious of the desert's illusions.")
            time.sleep(2)

        # Challenge 2: Sandstorm
        print("Challenge 2: Sandstorm")
        time.sleep(2)
        print("A massive sandstorm approaches, obscuring your vision and threatening to bury you in sand.")
        time.sleep(2)
        choice = input("Do you want to seek shelter and wait out the storm (1) or keep moving through the storm (2)? ")
        time.sleep(2)
        if choice == "1":
            print("You find shelter behind a large dune and wait for the storm to pass.")
            time.sleep(2)
            print("After the storm subsides, you emerge from your shelter and continue your journey.")
            time.sleep(2)
        elif choice == "2":
            print("You brave the sandstorm, pushing forward despite the harsh conditions.")
            time.sleep(2)
            print("With determination, you make it through the storm and continue your journey.")
            time.sleep(2)
        else:
            print("You hesitate, and the sandstorm engulfs you, making progress difficult.")
            time.sleep(2)
            print("After a grueling struggle, you manage to escape the storm, but the experience leaves you exhausted.")
            time.sleep(2)

        # Final Challenge: Desert Temple
        print("Final Challenge: Desert Temple")
        time.sleep(2)
        print("After overcoming numerous challenges, you discover a hidden desert temple, buried beneath the sands.")
        time.sleep(2)
        print("The temple holds ancient secrets and potential treasures, but also dangers.")
        time.sleep(2)
        choice = input("Do you want to explore the temple (1) or continue your journey without investigating (2)? ")
        time.sleep(2)
        if choice == "1":
            print("You decide to explore the temple, uncovering hidden chambers and ancient artifacts.")
            time.sleep(2)
            print("Among the treasures, you find a map leading to a hidden oasis, providing you with a crucial advantage.")
            time.sleep(2)
            print("Congratulations! You have conquered the Desert and discovered the secrets of the temple!")
            time.sleep(2)
        elif choice == "2":
            print("You decide to continue your journey, leaving the temple unexplored.")
            time.sleep(2)
            print("Although you miss out on potential treasures, you avoid the dangers hidden within the temple.")
            time.sleep(2)
            print("Your adventure continues...\n")
        else:
            print("You hesitate too long, and the temple's entrance collapses, sealing it off.")
            time.sleep(2)
            print("You continue your journey, determined to find other adventures.")
            time.sleep(2)

        print("Congratulations! You have conquered the Desert and braved its many challenges!")

    def game_jungle(self):
        print("Welcome to the Jungle! The thick foliage and the sounds of exotic wildlife surround you...")
        time.sleep(2)
        print("As you venture deeper into the jungle, you encounter a series of challenges.")
        time.sleep(2)
        
        # Challenge 1: Dense foliage
        print("Challenge 1: Dense foliage")
        time.sleep(2)
        print("The path ahead is blocked by dense foliage. You need to find a way through.")
        time.sleep(2)
        choice = input("Do you want to cut through the foliage with a machete (1) or find a way around it (2)? ")
        time.sleep(2)
        if choice == "1":
            print("You cut through the dense foliage, making slow but steady progress.")
            time.sleep(2)
        elif choice == "2":
            print("You find a way around the foliage, discovering a hidden path that speeds up your journey.")
            time.sleep(2)
        else:
            print("You hesitate too long, and the jungle's wildlife starts to stir, forcing you to move quickly.")
            time.sleep(2)

        # Challenge 2: River crossing
        print("Challenge 2: River crossing")
        time.sleep(2)
        print("You come across a wide river with fast-moving water. There's a fallen log that might serve as a bridge.")
        time.sleep(2)
        choice = input("Do you want to cross the river using the log (1) or look for another way across (2)? ")
        time.sleep(2)
        if choice == "1":
            print("You carefully balance across the log, managing to reach the other side safely.")
            time.sleep(2)
        elif choice == "2":
            print("You find a shallower part of the river and wade across, getting wet but staying safe.")
            time.sleep(2)
        else:
            print("You hesitate too long, and the river's current becomes too strong to cross safely.")
            time.sleep(2)

        # Challenge 3: Ancient temple
        print("Challenge 3: Ancient temple")
        time.sleep(2)
        print("You discover an ancient temple, hidden among the dense foliage.")
        time.sleep(2)
        choice = input("Do you want to explore the temple (1) or continue your journey without investigating (2)? ")
        time.sleep(2)
        if choice == "1":
            print("You decide to explore the temple, uncovering hidden chambers and ancient artifacts.")
            time.sleep(2)
            print("Among the treasures, you find a map leading to a hidden treasure deep within the jungle.")
            time.sleep(2)
        elif choice == "2":
            print("You decide to continue your journey, leaving the ancient temple unexplored.")
            time.sleep(2)
            print("Although you miss out on potential treasures, you avoid the dangers hidden within the temple.")
            time.sleep(2)
        else:
            print("You hesitate too long, and the temple entrance collapses, sealing it off.")
            time.sleep(2)
            print("You continue your journey, determined to find other adventures.")
            time.sleep(2)

        # Final Challenge: Jungle Waterfall
        print("Final Challenge: Jungle Waterfall")
        time.sleep(2)
        print("After overcoming numerous challenges, you reach a magnificent waterfall cascading down into a crystal-clear pool.")
        time.sleep(2)
        print("The waterfall marks the end of your jungle adventure, but there's one final challenge.")
        time.sleep(2)
        choice = input("Do you want to climb to the top of the waterfall (1) or swim in the pool at its base (2)? ")
        time.sleep(2)
        if choice == "1":
            print("You carefully climb the slippery rocks, making your way to the top of the waterfall.")
            time.sleep(2)
            print("From the top, you enjoy a breathtaking view of the jungle and feel a sense of accomplishment.")
            time.sleep(2)
        elif choice == "2":
            print("You dive into the pool, enjoying the refreshing water and the beauty of the waterfall.")
            time.sleep(2)
            print("After a relaxing swim, you feel rejuvenated and ready for your next adventure.")
            time.sleep(2)
        else:
            print("You hesitate too long, and the jungle's wildlife begins to stir, prompting you to leave quickly.")
            time.sleep(2)
            print("You continue your journey, leaving the jungle waterfall behind.")
            time.sleep(2)

        print("Congratulations! You have conquered the Jungle and braved its many challenges!")
        print("Your adventure continues...\n")

    def game_sky(self):
        print("Welcome to the Sky! The vast expanse of clouds and the endless blue horizon await you...")
        time.sleep(2)
        print("As you soar through the skies, you encounter a series of challenges.")
        time.sleep(2)
        
        # Challenge 1: Storm Clouds
        print("Challenge 1: Storm Clouds")
        time.sleep(2)
        print("You encounter a massive storm cloud blocking your path. Lightning crackles ominously.")
        time.sleep(2)
        choice = input("Do you want to navigate through the storm cloud (1) or find a way around it (2)? ")
        time.sleep(2)
        if choice == "1":
            print("You brave the storm, carefully navigating through the turbulent clouds.")
            time.sleep(2)
            print("With skill and determination, you make it through the storm unscathed.")
            time.sleep(2)
        elif choice == "2":
            print("You search for a safer route around the storm cloud, avoiding the dangerous lightning.")
            time.sleep(2)
            print("Although it takes longer, you safely bypass the storm and continue your journey.")
            time.sleep(2)
        else:
            print("You hesitate too long, and the storm engulfs you, buffeting you with wind and rain.")
            time.sleep(2)
            print("With great effort, you manage to escape the storm, but the experience leaves you shaken.")
            time.sleep(2)

        # Challenge 2: Floating Islands
        print("Challenge 2: Floating Islands")
        time.sleep(2)
        print("You come across a series of floating islands, each with unique landscapes and challenges.")
        time.sleep(2)
        choice = input("Do you want to explore the floating islands (1) or continue your journey (2)? ")
        time.sleep(2)
        if choice == "1":
            print("You explore the floating islands, discovering hidden treasures and breathtaking vistas.")
            time.sleep(2)
            print("Among the islands, you find valuable resources and clues to your next destination.")
            time.sleep(2)
        elif choice == "2":
            print("You decide to continue your journey, leaving the floating islands unexplored.")
            time.sleep(2)
            print("Although you miss out on potential discoveries, you make good progress in your journey.")
            time.sleep(2)
        else:
            print("You hesitate too long, and the floating islands drift apart, making exploration difficult.")
            time.sleep(2)
            print("You continue your journey, determined to find other adventures.")
            time.sleep(2)

        # Final Challenge: Sky Castle
        print("Final Challenge: Sky Castle")
        time.sleep(2)
        print("After overcoming numerous challenges, you discover a majestic sky castle floating among the clouds.")
        time.sleep(2)
        print("The castle holds ancient secrets and potential treasures, but also dangers.")
        time.sleep(2)
        choice = input("Do you want to explore the sky castle (1) or continue your journey without investigating (2)? ")
        time.sleep(2)
        if choice == "1":
            print("You decide to explore the sky castle, uncovering hidden chambers and ancient artifacts.")
            time.sleep(2)
            print("Among the treasures, you find a map leading to a hidden paradise among the clouds.")
            time.sleep(2)
            print("Congratulations! You have conquered the Sky and discovered the secrets of the sky castle!")
            time.sleep(2)
        elif choice == "2":
            print("You decide to continue your journey, leaving the sky castle unexplored.")
            time.sleep(2)
            print("Although you miss out on potential treasures, you avoid the dangers hidden within the castle.")
            time.sleep(2)
            print("Your adventure continues...\n")
        else:
            print("You hesitate too long, and the castle's entrance disappears among the shifting clouds.")
            time.sleep(2)
            print("You continue your journey, determined to find other adventures.")
            time.sleep(2)

        print("Congratulations! You have conquered the Sky and braved its many challenges!")
