from sc2.bot_ai import BotAI
from sc2.game_data import Cost
from sc2.units import UnitTypeId, Unit, Units

# Import Unit translator
from ..utility import ZergUnits



class Larva:
    # CHECK SECTION
    def enough_resource(min, gas, cost:Cost):
        return min >= cost.minerals and gas >= cost.vespene
        #
    def enough_supply(sup_left, sup_cost, prev_unit_cost, morph=False):
        # Apply morph supply cost reduction if morphin
        morph_reduction = prev_unit_cost if morph else 0
        #
        # Supply that is left is bigger or equal to the directive
        return sup_left >= (sup_cost - morph_reduction)
        #
        #
    # TRAIN SECTION
    def can_train(e_sup, e_res):
        return e_sup and e_res
        #
    def train(nyarka:BotAI, unit_id:UnitTypeId):
        success = nyarka.train(unit_type=unit_id)
        # :3
        return success
        #
        #
    # MAIN FUNCTION
    def run(nyarka:BotAI, obj):
        # Get resources
        minerals = nyarka.minerals
        gas = nyarka.vespene
        # Get Unit related data
        unit_id = ZergUnits.translate(obj)
        supply_left = nyarka.supply_left
        supply_cost = nyarka.calculate_supply_cost(unit_id)
        #
        #
        # CHECKS
        # Resources :3
        #
        enough_sup = Larva.enough_supply(
            sup_left=supply_left,
            sup_cost=supply_cost,
            prev_unit_cost=nyarka.calculate_supply_cost(ZergUnits.morph_protoplast(unit_id)),
            morph=ZergUnits.morphs(unit_id)
        )
        # Supply :3
        #
        enough_res = Larva.enough_resource(
            min=minerals,
            gas=gas,
            cost=nyarka.calculate_cost(unit_id)
        )
        #
        # 
        if Larva.can_train(e_sup=enough_sup, e_res=enough_res):
            return Larva.train(nyarka, unit_id) # Training successfull ?

        # Can't train so step can't be completed :/        
        return False
