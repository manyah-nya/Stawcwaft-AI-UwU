from sc2.bot_ai import BotAI

# Import Tasks
from .Tasks.build import Build
from .Tasks.upgrade import Upgrade
from .Tasks.larva import Larva
from .Tasks.incubate import Incubate
from .Tasks.spread import Spread


class TaskManager():
    def __init__(self, nyarka:BotAI):
        self.nyarka = nyarka

        # Dictionary for Specific Tasks
        self.task_dict = {
            "build": Build,
            "upgrade": Upgrade,
            "larva": Larva,
            "incubate": Incubate,
            "spread": Spread
        }


    def run(self, action_dir):
        self.task_dict[action_dir["task"]].run(self.nyarka, action_dir["obj"])
        pass
    