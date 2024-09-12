class Battle:
    
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy
    
    def do_battle(self, hero, enemy):
        while enemy.alive() == True and hero.alive() == True:
            self.hero.print_status()
            self.enemy.print_status()
            print("What do you want to do?")
            print(f"1. fight {enemy.name}")
            print("2. do nothing")
            print("3. flee")
            print("4. swap power")
            print("> ",)
            user_input = input()
            if user_input == "1":
                # Hero attacks enemy
                hero.attack(enemy)
                if enemy.health <= 0:
                    print(f"The {enemy.name} is dead.")
            elif user_input == "2":
                pass
            elif user_input == "3":
                print("Goodbye.")
                break
            elif user_input == "4":
                print(f"{hero.name} and {enemy.name} swapped powers!")
                self.hero.swap_power(enemy)
            else:
                print("Invalid input %r" % user_input)

            if enemy.alive() == True:
                # Goblin attacks hero
                enemy.attack(hero)
                if hero.alive() == False:
                    print("You are dead.")