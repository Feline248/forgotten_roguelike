class Item:

    def __init__(self, name:str, description:str, cost:int=0):
        self.name = name
        self.description = description
        self.cost = cost


class Weapon(Item):

    def __init__(self, name:str, description:str, cost:int, damage_multiplier:float, wield_requirement:int):
        Item.__init__(self, name, description)
        self.damage_multiplier = damage_multiplier
        self.wield_requirement = wield_requirement

class Armor(Item):

    def __init__(self, name:str, description:str, cost:int, hitpoints:int, variety:str, wield_requirement:int):
        Item.__init__(self, name, description)
        self.hitpoints = hitpoints
        self.variety = variety
        self.wield_requirement = wield_requirement

