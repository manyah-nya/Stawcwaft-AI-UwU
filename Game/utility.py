from numpy import random # For Map class

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
    def random(map_list): return map_list[random.randint(0, len(map_list))]
    def proper_id(id, map_length): return (0 <= id < map_length)
    def get(id, selection, map_list):
        if Map.proper_id(id, len(map_list)) and selection == "Id": return map_list[id]
        else: return Map.random(map_list)
    #
    #