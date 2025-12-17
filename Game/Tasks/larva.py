from sc2.bot_ai import BotAI
from sc2.units import UnitTypeId, Units, Unit






class Larva:
    def run(nyarka:BotAI, obj):
        minerals = nyarka.minerals
        supply_left = nyarka.supply_left
        supply_cost = nyarka.calculate_supply_cost(UnitTypeId.DRONE)

        print(obj)

        pass
