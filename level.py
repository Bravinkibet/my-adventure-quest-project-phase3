class Level:
    def __init__(self):
        self.levels = {
            1: ["Forest", "Cave", "Ruins"],
            2: ["Mountains", "Lake", "Castle"],
            3: ["Desert", "Volcano", "Ocean", "Island"],
            4: ["Jungle", "Tower", "Swamp", "Village"],
            5: ["Sky", "Maze", "Underworld", "Final Boss"]
        }

    def get_level_games(self, level_number):
        return self.levels.get(level_number, [])

    def get_total_levels(self):
        return len(self.levels)
