from Game.items import (weapons, armors, potions, Weapon, Armor, UseableItem)

class Entity:
    def __init__(self, name, health, strength, main_hand:Weapon=None, off_hand:Weapon=None,
                 helmet:Armor=None, chestplate:Armor=None, leggings:Armor=None, boots:Armor=None, inventory:list[UseableItem]=[], level=1,xp=0, max_xp=100):
        self.name = name
        self.health = health
        self.max_health = health
        self.strength = strength
        self.main_hand = main_hand
        self.off_hand = off_hand
        self.helmet = helmet
        self.chestplate = chestplate
        self.leggings = leggings
        self.boots = boots
        self.inventory = inventory
        self.level = level
        self.bestiary = {}
        self.xp = xp
        self.max_xp = max_xp
class Character(Entity):
    def __init__(self, name, health, strength, main_hand:Weapon=None, off_hand:Weapon=None,
                 helmet:Armor=None, chestplate:Armor=None, leggings:Armor=None, boots:Armor=None, inventory=[]):
        super().__init__(name, health, strength, main_hand, off_hand,
                        helmet, chestplate, leggings, boots, inventory)
        
# Création des personnages jouables
characters = {
"warrior" : Character("Guerrier", 100, 7,
                   main_hand=weapons["basic_sword"], off_hand=weapons["basic_shield"],
                   helmet=armors["helmet"], chestplate=armors["chestplate"], leggings=armors["leggings"], boots=armors["boots"],
                   inventory=[potions["health_potion"], potions["strenght_potion"]])

,"mage" : Character("Mage", 70, 8,
                main_hand=weapons["magic_staff"], off_hand=weapons["spell_book"],
                helmet=armors["helmet"], chestplate=armors["chestplate"], leggings=armors["leggings"], boots=armors["boots"],
                inventory=[potions["mana_potion"], potions["health_potion"]])

,"archer" : Character("Archer", 80, 10,
                  main_hand=weapons["wooden_bow"], off_hand=weapons["wooden_trap"],
                  helmet=armors["helmet"], chestplate=armors["chestplate"], leggings=armors["leggings"], boots=armors["boots"],
                  inventory=[potions["health_potion"]])

,"easteregg" : Character("Secret", 999, 998,
                     main_hand=weapons["basic_sword"], off_hand=weapons["basic_shield"],
                     helmet=armors["helmet"], chestplate=armors["chestplate"], leggings=armors["leggings"], boots=armors["boots"])
    
    
}


class Enemy(Entity):
    def __init__(self, name, health, strength, main_hand=None, off_hand=None,
                 helmet=None, chestplate=None, leggings=None, boots=None, level=1):
        super().__init__(name, health, strength, main_hand, off_hand,
                        helmet, chestplate, leggings, boots, level=level)

# Création des ennemis
enemies = {
"gobelin" : Enemy("Gobelin", 45, 5, main_hand=weapons["poignard"], level=1)
,"orque" : Enemy("Orque", 70, 15, main_hand=weapons["gourdin"], off_hand=weapons["basic_shield"], level=1)
,"troll" : Enemy("Troll", 120, 30,
             main_hand=weapons["axe"], off_hand=weapons["basic_shield"],
             helmet=armors["helmet"], chestplate=armors["chestplate"],
             leggings=armors["leggings"], boots=armors["boots"], level=1)
}
 