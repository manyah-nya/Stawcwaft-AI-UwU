from sc2.bot_ai import BotAI


class Reporter():
    def __init__(self, nyarka:BotAI):
        self.nyarka = nyarka

    # Game data
    def game(self, iteration):
        # print(
        #     f"Iteration: {iteration}\n",
        #     f"Drones: {self.nyarka.workers.amount}, Idle Drones: {self.nyarka.workers.idle.amount}\n",  
        #     f"Minerals: {self.nyarka.minerals}, Gas: {self.nyarka.vespene}, Supply: {self.nyarka.supply_used}/{self.nyarka.supply_cap}\n"
        #     f"------------------------------------------------------------------"
        # )
        pass
    

    def ai(self, iteration):
        pass


    def run(self, iteration):
        self.ai(iteration)
        self.game(iteration)