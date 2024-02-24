
class Player():
    DEFAULT_APPEARANCE = None

    def __init__(self):
        self.x_position = 250
        self.y_position = 250
        self.location = "tutorial"
        self.health = 25
        self.attack_damage = 1
        self.experience = 0

    def move(self, direction:str):
        """move player one(1) tile in the specified direction"""
        pass

    def attack(self, target:Enemy):
        """Attack an enemy"""
        pass

    def buy(self, item:Item):
        """buy an item"""
        pass
    
    def equip_weapon(self, weapon:Weapon):
        """equip a new weapon and put the old one back in inventory"""
        pass

    def equip_armor(self, armor:Armor):
        """equip new armor and put the old one back in inventory if necessary"""
        pass

    def be_injured(self, damage:int):
        """reduce player health when hit by an enemy"""
        pass

    def die(self):
        """end game when health reaches 0"""
        pass

    def heal(self, health:int):
        """increase health"""
        pass

    def interact(self, interactable):
        """interact with a non-aggressive person or object"""
        pass

    def level_up(self):
        """increase health and attack damage"""
        self.max_health += 5
        self.attack_damage += 3