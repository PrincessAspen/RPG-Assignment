from character import Character, Hero, Enemy
from store import Store, Item, Tonic, Sword
from battle import Battle
import random


"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""


def main():
    hero = Hero("Hero")
    goblin = Enemy("Goblin")
    goblin.alive()
    hero.alive()
    goblin_battle = Battle(hero, goblin)
    goblin_battle.do_battle(hero, goblin)

main()