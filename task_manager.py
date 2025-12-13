from sc2.bot_ai import BotAI

class TaskManager():
    def __init__(self, nya_bot:BotAI):
        self.xd = 1

        print(
            f"Minerals from build manager: {nya_bot.minerals}",
            f"Workers from manager: {nya_bot.workers.amount}"
            )
    