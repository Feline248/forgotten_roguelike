import pygame
import attacks

class Creature():

    def __init__(self, image:str, move_pattern:str, aggressive:bool):
        self.image = pygame.image.load(os.path.join("graphics", image))
        self.move_pattern = move_pattern
        self.aggressive = aggressive


class Character(Creature):

    def __init__(self, name:str, image:str, move_pattern:str="stationary"):
        Creature.__init__(self, image, move_pattern, aggressive=False)
        self.name = name


class Monster(Creature):

    def __init__(self, type:str, image:str, health:int, move_pattern:str):
        Creature.__init__(self, image, move_pattern, aggressive=True)
        self.type = type
        self.health = health
        self.attacks = self.type["attacks"]
        self.attack_damages = self.type["attack_damages"]
        self.attack_animations = self.type["attack_animations"]
        self.attack_frequencies = self.type["attack_frequencies"]



class Boss(Character, Monster):

    #TODO figure out how multiple inheritance works
    pass

