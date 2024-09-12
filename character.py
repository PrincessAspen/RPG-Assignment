import random

class Character:
    def __init__(self, name, health=1, power=1, coins=20):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins
    
    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.power} power.")
        
    def attack(self, opponent):
        opponent.health -= self.power
        
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
        
    def swap_power(self, opponent):
        first = self.power
        second = opponent.power
        self.power = second
        opponent.power = first

class Hero(Character):
    def __init__(self, name, health=10, power=5):
        super().__init__(name, health, power, 20)
        self.items = []
        
    def attack(self, opponent):
        critical = random.random()
        if critical < .2:
            print(f"{self.name} deals a critical hit to the {opponent.name}! They take {self.power*2} damage!")
            opponent.health -= self.power*2
        else:
            print(f"{self.name} attacks the the {opponent.name}! They take {self.power} damage!")
            super().attack(opponent)
        
    def buy(self, item):
        self.coins = self.coins - item.cost
        self.items.append(item)
            
class Enemy(Character):
    def __init__(self, name, health=6, power=2, bounty=10):
        super().__init__(name, health, power)
        self.bounty = bounty
        
    def attack(self, opponent):
        print(f"The {self.name} attacks {opponent.name}! They take {self.power} damage!")
        super().attack(opponent)
