# Sc2 importing
from sc2.bot_ai import BotAI # Parent class
from sc2.player import Player, Bot, Computer # Wrapper for the agent
from sc2.data import Race, Difficulty
from sc2.main import run_game # Function that starts a game
from sc2 import maps # For loading maps


# Other importing
import os


# File importing (Relational Stuff :3)
from Game.task_manager import TaskManager
from Game.settings import Settings
from Game.reporter import Reporter
from Game.build_order import BuildOrder
import config


# Var initialisation
settings = Settings()



class Nyarka(BotAI): # NyaBot UwU kawaii :3
    def __init__(self):
        self.task_manager = TaskManager(self)
        self.build_order = BuildOrder(self)
        self.reporter = Reporter(self)


    async def on_start(self):
        pass


    async def on_step(self, iteration:int): # is called every step/tick of the game
        if settings.reports: self.reporter.run(iteration) # Print stats of the game
        
        
        # Logic
        pass



# Check if in correct file :3
if __name__ == "__main__":
    # See settings
    print(settings.map)

    run_game(
        maps.get(settings.map),
        [
            Bot(
                Race[config.NYARKA_RACE],
                Nyarka()
            ),
            Computer(
                Race[settings.enemy_race],
                Difficulty[settings.enemy_difficulty]
            )
        ],
        realtime=settings.realtime # Makes agent not bound to step execution time.
    )


