from random import choice
from creature import Character, Monster, Boss

class Room():

    def __init__(self, location:str, tileset:list[Tile], dimensions:list[int], monsters:list[Monster]): #dimensions is a list in the form of [height, width] in units of tiles
        self.location = location
        self.tileset = tileset
        self.monsters = monsters
        self.set_up_tiles()
        self.add_monsters(self)

    def set_up_tiles(self):
        """arrange tiles in random order"""
        for i in range(self.dimensions(0)):
            for j in range (self.dimensions(1)):
                pass

    def add_monsters(self):
        """fill room with monsters"""
        for monster in self.monsters:
            pass

    def add_item(self, item:Item):
        """put an item somewhere in the room"""
        pass


class SkillRoom(Room):
    """skill rooms require the player to solve a puzzle
    in order to learn a new skill"""

    def __init__(self, location:str, tileset:list[Tile], dimensions:list[int]):
        Room.__init__(self, location, tileset, dimensions, monsters=[])

    #TODO figure out how to implement puzzles


class ExitRoom(Room):
    """exit rooms allow the player to move to the next 
    level if the flash drive has been found"""

    def __init__(self, location:str, tileset:list[Tile], dimensions:list[int], monsters:list[Monster]):
        Room.__init__(self, location, tileset, dimensions, monsters)


class ChallengeRoom(Room):
    """challenge rooms are extra difficult rooms that 
    contain the flashdrive the player uses to unlock 
    the door to the next level"""

    def __init__(self, location:str, tileset:list[Tile], dimensions:list[int], monsters:list[Monster]):
        Room.__init__(self, location, tileset, dimensions, monsters)



class ShopRoom(Room):

    def __init__(self, location:str, tileset:list[Tile], dimensions:list[int]):
        Room.__init__(self, location, tileset, dimensions, monsters=[])


class CharacterRoom(Room):

    def __init__(self, location:str, tileset:list[Tile], dimensions:list[int], character:Character):
        Room.__init__(self, location, tileset, dimensions, monsters=[])
