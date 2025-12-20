# SC2 specific 
from sc2.bot_ai import BotAI
from .utility import File


# Basic Imports
from numpy import random
import config
import json




class BuildOrder():
    # INIT
    def __init__(self, nyarka:BotAI):
        self.nyarka = nyarka # Remember the bot :3
        self.data = File.load(config.BUILD_ORDERS_PATH) # Load build orders from the json
        self.current_build = None
        self.current_step_index = None # Current step of the chosen build
        self.state = True # If true -> Active, If false -> Turned off
        #
        #
        #
    # GET SECTION
    # Get specific build from self.data (build_order.json)
    def get_build(self, builds, e_race, build_directive):
        build_category = builds[e_race]
        #
        # Decide which build should be used based on directive (WIP)
        build_strategy = random.randint(0, len(build_category)) # To change
        #
        # Return current build
        return build_category[build_strategy]
        #
    # Run every time brain decides it's current build is outdated
    def update_build(self, build_directive):
        # 
        if build_directive == None:
            raise ValueError("directive does not exist")
        #
        # Get current build :P
        # Based on directive (now nonexistant)
        self.current_build = self.get_build(
            builds = self.data,
            e_race = self.nyarka.enemy_race.name,
            build_directive = build_directive
        )
        #
        self.current_step_index = 0 # Reset action index
        #
        #
    # UPDATE SECTION
    # Check if current build was completed
    def step_ended(self, completed):
        if completed: self.current_step_index += 1
        #
    def ended(self):
        return self.current_step_index >= len(self.current_build["steps"])
        #
        #