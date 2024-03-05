
class Player():
    DEFAULT_APPEARANCE = None

    def __init__(self):
        self.x_position = 250
        self.y_position = 250
        self.location = "tutorial"
        self.max_health = 25
        self.health = self.max_health
        self.base_attack_damage = 1
        self.attack_damage = self.base_attack_damage
        self.experience = 0
        self.money = 0
        self.level = 1
        self.inventory = []
        self.weapon = Weapon("pocketknife", "A trusty multitool that has never served you wrong", 1)

    def move(self, direction:str):
        """move player one(1) tile in the specified direction"""
        pass

    def attack(self, target:Enemy):
        """Attack an enemy"""
        pass

    def buy(self, item:Item):
        """buy an item and add it to inventory"""
        self.money -= item.cost
        self.inventory.append(item)
    
    def equip_weapon(self, new_weapon:Weapon):
        """equip a new weapon and put the old one back in inventory"""
        self.inventory.remove(new_weapon)
        self.inventory.append(self.weapon)
        self.weapon = new_weapon
        self.attack_damage = self.base_attack_damage * weapon.damage_multiplier

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
        self.health += health

    def pick_up(self, item:Item):
        self.inventory.append(item)

    def interact(self, interactable):
        """interact with a person or object
        type of interactable argument determines response"""

        if type(interactable) == Creature and interactable.aggressive == True:
            self.attack(interactable)

        if type(interactable) == Creature and interactable.aggressive == False:
            pass

        if type(interactable) == Item and interactable.grabbable == True:
            self.pick_up(interactable)


    def level_up(self):
        """increase health and attack damage"""
        if self.level < 10:
            self.level += 1
            self.max_health += 5
            self.attack_damage += 3