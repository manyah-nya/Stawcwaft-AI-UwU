# Sc2 importing
from sc2.bot_ai import BotAI # Parent class
from sc2.data import Difficulty, Race # Sc2 built in bots
from sc2.player import Player, Bot, Computer # Wrapper for the agent
from sc2.main import run_game # Function that starts a game
from sc2 import maps # For loading maps

# Other importing
import random
import json


# File importing
from task_manager import TaskManager



# Static data points
game_race_list = [Race.Zerg, Race.Protoss, Race.Terran]
game_map_list = ["IncorporealAIE_v4", "LeyLinesAIE_v3", "PersephoneAIE_v4", "PylonAIE_v4", "TorchesAIE_v4"]


# Settings
game_map = game_map_list[1]
game_difficulty = Difficulty.Hard
game_race = game_race_list[random.randrange(0,3)]




class NyaBot(BotAI): # NyaBot UwU kawaii :3
    async def on_start(self):
        self.task_manager = TaskManager(self)


    async def on_step(self, iteration:int): # is called every step/tick of the game
        # Print stats of the game
        print(
            f"Iteration: {iteration}\n",
            f"Drones: {self.workers.amount}, Idle Drones: {self.workers.idle.amount}\n",  
            f"Minerals: {self.minerals}, Gas: {self.vespene}, Supply: {self.supply_used}/{self.supply_cap}\n"
            f"------------------------------------------------------------------"
        )

        print(self.task_manager.xd)
        # Logic





run_game(
    maps.get(game_map),
    [
        Bot(Race.Zerg, NyaBot()),
        Computer(game_race, game_difficulty)],
    realtime=False, # Makes agent not bound to step execution time.
)


