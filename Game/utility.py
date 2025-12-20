from numpy import random # For Map class
from sc2.units import UnitTypeId

# So that stuff works
import os
import json



class File:
    def load(path):
        try:
            with open(path, 'r') as file:
                data = json.load(file)
                return data
            
        except FileNotFoundError:
            print(f"Error: file {path} was not found.")
        

        file.close() # Close :3
    #   
    #
class Directory:
    # List file in specific directory and turn them into a file
    def list_files(path, extension=""):
        filename_list = []
        
        # Run through the whole direcotry and extract
        for file in os.listdir(path):
            if file.endswith(f".{extension}"):
                filename_list.append(file.split(".")[0]) # Append with name without the extension

        return filename_list
    #
    #
class Map:
    #
    def random(map_list):
        return map_list[random.randint(0, len(map_list))]
    #
    def proper_id(id, map_length): 
        return (0 <= id < map_length)
    #
    #
    def get(id, selection, map_list):
        if Map.proper_id(id, len(map_list)) and selection == "Id": return map_list[id]
        else: return Map.random(map_list)
    #
    #
class ZergUnits:
    dicionary = {
        "overlord": UnitTypeId.OVERLORD,
        "overseer": UnitTypeId.OVERSEER,
        "drone": UnitTypeId.DRONE,
        "zergling": UnitTypeId.ZERGLING,
        "queen": UnitTypeId.QUEEN,
        "roach": UnitTypeId.ROACH,
        "baneling": UnitTypeId.BANELING,
        "ravager": UnitTypeId.RAVAGER,
        "mutalisk": UnitTypeId.MUTALISK,
        "corruptor": UnitTypeId.CORRUPTOR,
        "hydralisk": UnitTypeId.HYDRALISK,
        "infestor": UnitTypeId.INFESTOR,
        "swarmhost": UnitTypeId.SWARMHOSTMP, # Idk if that's the correct id :/
        "lurker": UnitTypeId.LURKER,
        "ultralisk": UnitTypeId.ULTRALISK,
        "broodlord": UnitTypeId.BROODLORD
    }
    require_larva = [
        UnitTypeId.OVERSEER,
        UnitTypeId.DRONE,
        UnitTypeId.ZERGLING,
        UnitTypeId.ROACH,
        UnitTypeId.MUTALISK,
        UnitTypeId.CORRUPTOR,
        UnitTypeId.HYDRALISK,
        UnitTypeId.INFESTOR,
        UnitTypeId.SWARMHOSTMP, # Same thing :/
        UnitTypeId.ULTRALISK
    ]
    require_morphin = [
        UnitTypeId.OVERSEER,
        UnitTypeId.BANELING,
        UnitTypeId.RAVAGER,
        UnitTypeId.LURKER,
        UnitTypeId.BROODLORD,

    ]
    morphs_from = {
        UnitTypeId.OVERSEER: UnitTypeId.OVERLORD,
        UnitTypeId.BANELING: UnitTypeId.ZERGLING,
        UnitTypeId.RAVAGER: UnitTypeId.ROACH,
        UnitTypeId.LURKER: UnitTypeId.HYDRALISK,
        UnitTypeId.BROODLORD: UnitTypeId.CORRUPTOR
    }

    def morph_protoplast(unit_id:UnitTypeId):
        if unit_id in ZergUnits.morphs_from:
            return ZergUnits.morphs_from[unit_id]
        #
        return UnitTypeId.CHANGELING # Return a changeling :3 cause morhps def will cancel it out.
        # Also Changeling supply cost is 0 :P
        #
    #
    # For units that get created through morphing
    def morphs(unit_id:UnitTypeId):
        return unit_id in ZergUnits.require_morphin
    #
    # For units that come from larva
    def incubates(unit_id:UnitTypeId):
        return unit_id in ZergUnits.require_larva
    #
    def translate(unit_id:str): 
        try: 
            return ZergUnits.dicionary[unit_id]
        except:
            raise KeyError(f"{unit_id} did not match any of ZergUnits.dictionary keys...")