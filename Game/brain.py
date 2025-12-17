from sc2.bot_ai import BotAI

# Import build orders
from .build_order import BuildOrder
from .task_manager import TaskManager



class Brain():
    def __init__(self, nyarka:BotAI):
        self.nyarka = nyarka # Bot :3
        
        # Brain parts initialization
        self.build_order = BuildOrder(nyarka)
        self.task_manager = TaskManager(nyarka)
        #
        # Brain states
        self.follow_build = True
        self.under_attack = False
        self.attacking = False


    def start(self):
        # See if there is any build order chosen
        if self.build_order.current_build == None:
            self.build_order.update_build(build_directive="CHANGETHISVALUE") # for now brain directive is nonexistant
        #

        #
        #
        #
    def run(self):
        # DECIDE WHAT TO DO xD
        # See if build order ended
        if self.build_order.ended():
            self.follow_build = False
        

        step = self.build_order.current_build["steps"][self.build_order.current_step_index]
        action_directive = step["directive"]
        print(step)

        # LOGIC
        # Build Order sh##
        if self.follow_build:
            if step["supply"] != self.nyarka.supply_used:
                self.task_manager.run(action_directive)
    