from sc2.bot_ai import BotAI

# Import build orders
from .build_order import BuildOrder
from .task_manager import TaskManager


# INDEPENDENT
# This class has premade tasks. 
# They do not need build order to function.
from .Tasks.independent import Independent


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
        iteration = self.nyarka._total_steps_iterations

        # Print data about current task to see xD
        if iteration % self.nyarka.settings.reports_i == 0:
            print(f"-----------Iteration: {iteration}-----------")
            print(step)

        # LOGIC
        # Build Order sh##
        if self.follow_build:
            # Have to add possibility of custom tasks that are
            # Independent despite build order
            # 
            # If supply is equal to the one required for next step --- execute:
            if step["supply"] == self.nyarka.supply_used:
                completed = self.task_manager.run(action_directive) # Has completed the task ?
                #
                # On success proceed with build order
                self.build_order.step_ended(completed)
                #
            else:
                self.task_manager.run(Independent.get("drone")) # Do some droning for now
                # Make brain do some shit idk xD

