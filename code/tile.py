import os

class Tile():

    def __init__(self, image:str, permeability:bool): #if permeability is set to True, the player and non-flying enemies can stand on/walk through that tile
        self.image = pygame.image.load(os.path.join("graphics", image))
        self.permeability = permeability

class TrapTile(Tile):

    def __init__(self, image:str, trap_type:str):
        Tile.__init__(self, image, permeability=True)
        self.trap_type = trap_type

