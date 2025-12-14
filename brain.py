# Sc2 importing
from sc2.bot_ai import BotAI # Parent class
from sc2.player import Player, Bot, Computer # Wrapper for the agent
from sc2.data import Race, Difficulty
from sc2.main import run_game # Function that starts a game
from sc2 import maps # For loading maps


# Other importing


# File importing
from task_manager import TaskManager
from Game.utility import Reporter, Settings


# Var initialisation
settings = Settings()


class Nyarka(BotAI): # NyaBot UwU kawaii :3
    def __init__(self):
        self.task_manager = TaskManager(self)
        self.reporter = Reporter(self)


    async def on_start(self):
        pass


    async def on_step(self, iteration:int): # is called every step/tick of the game
        if settings.reports_active: # Print stats of the game
            self.reporter.run(iteration, settings)
        
        
        # Logic
        pass


print(settings.map)

run_game(
    maps.get(settings.map),
    [
        Bot(
            Race[settings.nyarka_race],
            Nyarka()
        ),
        Computer(
            Race[settings.enemy_race],
            Difficulty[settings.enemy_difficulty]
        )
    ],
    realtime=False, # Makes agent not bound to step execution time.
)


