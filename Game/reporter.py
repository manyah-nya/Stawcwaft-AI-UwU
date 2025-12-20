from sc2.bot_ai import BotAI


class Reporter():
    def __init__(self, nyarka:BotAI):
        self.nyarka = nyarka

    # Game data
    def game(self, iteration):
        if iteration % self.nyarka.settings.reports_i == 0:
            print(
                f"Status:\n"
                f"-----Following_Build: {self.nyarka.brain.follow_build}\n"
                f"-----Under_Attack: {self.nyarka.brain.under_attack}\n"
                f"-----Attacking: {self.nyarka.brain.attacking}\n"
                f"-----Current Step: {self.nyarka.brain.build_order.current_step_index}\n"
                f"Second: {round(self.nyarka.time)}\n"
                f"----------------------------------"
            )
        pass
    

    def ai(self, iteration):
        pass


    def run(self, iteration):
        self.ai(iteration)
        self.game(iteration)