# Sc2 importing
from sc2.bot_ai import BotAI # Parent class
from sc2.player import Player, Bot, Computer # Wrapper for the agent
from sc2.data import Race, Difficulty
from sc2.main import run_game # Function that starts a game
from sc2 import maps # For loading maps


# Other importing
import os


# File importing (Relational Stuff :3)
from Game.brain import Brain
from Game.settings import Settings
from Game.reporter import Reporter
import config


# Var initialisation
settings = Settings()



class Nyarka(BotAI): # NyaBot UwU kawaii :3
    def __init__(self):
        self.brain:Brain = Brain(self)
        self.reporter = Reporter(self)

        # Get those settings in :3
        self.settings = settings
        

    async def on_start(self):
        self.brain.start()


    async def on_step(self, iteration:int): # is called every step/tick of the game
        # LOGIC
        #
        self.brain.run()
        #
        # REPORTING
        if settings.reports and iteration % self.settings.reports_i == 0: self.reporter.run(iteration)



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


