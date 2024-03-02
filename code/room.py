from random import choice

class Room():

    def __init__(self, location:str, tileset:list, dimensions:list, safe:bool, difficulty:int): #dimensions is a list in the form of [height, width] in units of tiles
        self.location = location
        self.tileset = tileset
        self.safe = safe
        self.set_up_tiles()
        if self.safe == False:
            self.add_monsters(self)

    def set_up_tiles(self):
        """arrange tiles in random order"""
        for i in range(self.dimensions(0)):
            for j in range (self.dimensions(1)):
                pass

    def add_monsters(self):
        pass

    def add_item(self, item:Item):
        pass


class SkillRoom(Room):

    def __init__(self):
        pass


class ExitRoom(Room):

    def __init__(self):
        pass


class ChallengeRoom(Room):

    def __init__(self):
        pass


class ShopRoom(Room):

    def __init__(self):
        pass


class CharacterRoom(Room):

    def __init__(self):
        pass