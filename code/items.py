class Item:

    def __init__(self, name:str, description:str):
        self.name = name
        self. description = description


class Weapon(Item):

    def __init__(self, name:str, description:str, damage_multiplier:float, wield_requirement:int):
        Item.__init__(self, name, description)
        self.damage_multiplier = damage_multiplier
        self.wield_requirement = wield_requirement

class Armor(Item):

    def __init__(self, name:str, description:str, hitpoints:int, variety:str, wield_requirement:int):
        Item.__init__(self, name, description)
        self.hitpoints = hitpoints
        self.variety = variety
        self.wield_requirement = wield_requirement

