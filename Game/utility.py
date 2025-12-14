# Importing shit and stuff
from sc2.bot_ai import BotAI
from numpy import random

import os
import json




class File:
    def load(path):
        pass
    #
    #
class Directory:
    # List file in specific directory and turn them into a file
    def list_files(path, extension=""):
        filename_list = []
        
        # Run through the whole direcotry and extract
        for file in os.listdir(path):
            if file.endswith(f".{extension}"):
                filename_list.append(file.split(".")[0]) # Append with name without the extension

        return filename_list
    #
    #
class Map:
    def random(map_list): return map_list[random.randint(0, len(map_list))]
    def proper_id(id, map_length): return (0 <= id < map_length)
    def get(id, selection, map_list):
        if Map.proper_id(id, len(map_list)) and selection == "Id": return map_list[id]
        else: return Map.random(map_list)
    #
    #
class Settings():
    # Location of settings.json --- DO NOT CHANGE!!!
    settings_file = "./Data/Game/settings.json"

    def __init__(self): self.load()
    def load(self):
        try:
            with open(self.settings_file, 'r') as file:
                data = json.load(file)

            print(json.dumps(data, indent=4)) # Print settings

        except FileNotFoundError:
            print(f"Error: file {self.settings_file} was not found.")

        
        # Set the setttings:
        self.map_list = Directory.list_files(data["map_dir"], extension="SC2Map")
        self.map = Map.get(data["map_id"], data["map_selection"], self.map_list)
        self.reports_active = data["reports"]
        self.realtime_active = data["realtime"]
        self.enemy_race = data["enemy_race"]
        self.enemy_difficulty = data["enemy_difficulty"]

        self.nyarka_race = data["nyarka_race"]
        
        #-------------------------------------------------#
        file.close() 
    #
    #
class Reporter():
    def __init__(self, nya_bot:BotAI):
        self.bot = nya_bot

    # Game data
    def game(self, iteration):
        print(
            f"Iteration: {iteration}\n",
            f"Drones: {self.bot.workers.amount}, Idle Drones: {self.bot.workers.idle.amount}\n",  
            f"Minerals: {self.bot.minerals}, Gas: {self.bot.vespene}, Supply: {self.bot.supply_used}/{self.bot.supply_cap}\n"
            f"------------------------------------------------------------------"
        )
    

    def ai(self, iteration):
        print("")


    def run(self, iteration, settings):
        self.ai(iteration)
        self.game(iteration)