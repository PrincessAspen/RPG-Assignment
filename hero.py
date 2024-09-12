#Defines the hero and any other heroes in case I want to make them later
class Hero:
    def __init__(self, name, health=10, power=5):
        self.health = health
        self.power = power
        
    def hero_status(self):
        print(f"You have {self.health} health and {self.power} power.")
        
    def attack(self, enemy):
        print(f"You swing your weapon at the {enemy.name}! They take {self.power} damage!")
        enemy.health -= self.power
        
    def alive(self):
        if self.health <= 0:
            return False
        else:
            return True
            