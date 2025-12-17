from .utility import File, Directory, Map
import config
import json

class Settings():
    def __init__(self): self.load()
    def load(self):
        data = File.load(config.SETTINGS_PATH) # Get the json settings file


        print(json.dumps(data, indent=4)) # Print Settings
        

        # SETTINGS INITIALIZATION:
        # Get list of maps
        self.map_list = Directory.list_files(
            config.SC2_MAPS_PATH,
            extension=config.SC2_MAPS_EXTENSION
        )
        #
        # Check if map_list is not empty
        if self.map_list == []:
            raise FileNotFoundError(f"There are no maps in {config.SC2_MAPS_PATH} folder")
        #
        # Get the specific map for the game
        self.map = Map.get(
            data["map_id"],
            data["map_selection"],
            self.map_list
        )
        #
        # Initialize other settings data
        self.reports = data["reports"] # If true AI will report in-game data and stats.
        self.realtime = data["realtime"] # If true game will be run in realtime.
        self.enemy_race = data["enemy_race"] # What's the enemy's race.
        self.enemy_difficulty = data["enemy_difficulty"] # Enemy's difficulty
        #--------------------------------------#