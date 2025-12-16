from sc2.bot_ai import BotAI
from .utility import File
from numpy import random

import config
import json


class BuildOrder():
    def __init__(self, nyarka:BotAI):
        self.nyarka = nyarka # Remember the bot :3
        self.data = File.load(config.BUILD_ORDERS_PATH) # Load build orders from the json


        # Print a random build order:
        print(json.dumps(self.data["NvR"][0]["Title"], indent=4))


    def run():
        pass