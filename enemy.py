class Enemy:
    def __init__(self, name, health=6, power=2):
        self.name = name
        self.health = health
        self.power = power
        
    def enemy_status(self):
        print(f"{self.name} has {self.health} health and {self.power} power.")
        
    def enemy_attack(self, protagonist):
        print(f"The {self.name} attacks you! You take {self.power} damage!")
        protagonist.health -= self.power
        
    def alive(self):
        if self.health <= 0:
            return False
        else:
            return True
    