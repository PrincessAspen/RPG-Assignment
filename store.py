

class Store:
    def __init__(self, items):
        self.items = []
        
    def add_item(self, item):
        self.items.append(item)
        
    def do_shopping(self, hero):
        print("Welcome to the shop! You have {hero.coins} coins remaining.")
        for item in self.items:
            print(f"{item.name}: {item.cost} coins")
        
class Item:
    def __init__(self, name, cost=0):
        self.name = name
        self.cost = cost
        
    def apply(self, name, hero):
        #Due to the varied effect of items, I don't think a universal apply method works but I have it here just in case
        print(f"{hero.name} used {self.name}!")
        
class Tonic(Item):
    def __init__(self, name, cost=10, strength=2):
        super().__init__(name, cost)
        self.strength = strength
        
    def apply(self, name, hero):
        super().apply()
        hero.health += self.strength
        
class Sword(Item):
    def __init__(self,  name, cost=10, strength=2):
        super().__init__(name, cost)
        self.strength = strength
        
    def apply(self, name, hero):
        super().apply()
        hero.power += self.strength
        