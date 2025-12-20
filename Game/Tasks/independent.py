class Independent:
    drone = {
        "task": "larva",
        "obj": "drone"
    }
    more_supply = {
        "task": "larva",
        "obj": "overloard"
    }


    def get(task:str):
        t_dict = {
            "drone": Independent.drone,
            "more_supply": Independent.more_supply
        }
        # GET
        try:
            return t_dict[task]
        except:
            raise KeyError(f"{task} is not a valid 'Independent' task")