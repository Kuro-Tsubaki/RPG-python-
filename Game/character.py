from Game.items import (weapons, armors, potions, Weapon, Armor, UseableItem)
import random
class Entity:
    def __init__(self, name, health, strength, main_hand:Weapon=None, off_hand:Weapon=None,
                 helmet:Armor=None, chestplate:Armor=None, leggings:Armor=None, boots:Armor=None, inventory:list[UseableItem]=[], level=1,xp=0, max_xp=100, base_xp=0):
        self.name = name
        #Stat
        self.health = health
        self.max_health = health
        self.strength = strength
        #Stuff
        self.main_hand = main_hand
        self.off_hand = off_hand
        self.helmet = helmet
        self.chestplate = chestplate
        self.leggings = leggings
        self.boots = boots
        self.inventory = inventory
        #----
        self.bestiary = {}
        #leveling 
        self.level = level
        self.base_xp = base_xp
        self.xp = xp
        self.max_xp = max_xp
        self.active_buffs = {}
        #---
       
    def gain_xp(self, amount):
        self.xp += amount
        print(f"✨ XP : +{amount} (Total: {self.xp}/{self.max_xp})")
        # Cap for not skipping two level in one row
        while self.xp >= self.max_xp:
            self.level_up()

    def level_up(self):
        self.xp -= self.max_xp
        self.level += 1
        #Next level 25% harder
        self.max_xp = int(self.max_xp * 1.25)
        
        # Up stats
        self.max_health += 15
        self.health = self.max_health
        self.strength += 2
        
        print(f"\n🌟 PASSAGE AU NIVEAU {self.level} ! 🌟")
        print(f"Stats : ❤️ PV {self.max_health} | 💪 Force {self.strength}")
        print(f"🆙 Prochain niveau à : {self.max_xp} XP\n")
        
    def use_item(self, item):
        if not isinstance(item,UseableItem):
            print(f"L'objet {item.name} n'est pas utilisable !")
            return False
        
        item_stat = getattr(self,item.stat_to_fix)
        up_stat = item_stat + item.effect
        if item.stat_to_fix == "health":
            up_stat = min(up_stat, self.max_health)
        setattr(self, item.stat_to_fix, up_stat)
        
        stats_permanentes = ["health", "mana", "luck"]
        if item.stat_to_fix not in stats_permanentes:
            self.active_buffs[item.stat_to_fix] =  self.active_buffs.get(item.stat_to_fix,0) + item.effect 
        print(f"-> {self.name} utilise {item.name} (+{item.effect} {item.stat_to_fix})\n")
        self.inventory.remove(item)
        item_stat_after_use = getattr(self, item.stat_to_fix)
        print(f"{self.name} utilise {item.name} !")
        print(f"{item.stat_to_fix} : {item_stat} -> {item_stat_after_use}\n")
        return True
                
class Character(Entity):
    def __init__(self, name, health, strength, main_hand:Weapon=None, off_hand:Weapon=None,
                 helmet:Armor=None, chestplate:Armor=None, leggings:Armor=None, boots:Armor=None, inventory=[],level=1, base_xp=0, gold = 100):
        super().__init__(name, health, strength, main_hand, off_hand,
                        helmet, chestplate, leggings, boots, inventory,level=level, base_xp=base_xp)
        self.gold = gold
        
        
    def calculate_experience_gain(self, enemy):
        base_xp = enemy.base_xp
        
        if enemy.level > self.level:
            rank_multiplier = 2.0
            random_bonus = int(self.max_xp * 0.10) 

        elif enemy.level < int(self.level * 0.7): 
            rank_multiplier = 0.6
            random_bonus = 0

        else:
            rank_multiplier = 1.0
            random_bonus = random.randint(1, 5)
        
        total_xp = int((base_xp * rank_multiplier) + random_bonus)
        self.gain_xp(total_xp)
        return total_xp
            
            
characters = {
"warrior" : Character("Guerrier", 100, 8,
                   main_hand=weapons["basic_sword"], off_hand=weapons["basic_shield"],
                   helmet=armors["helmet"], chestplate=armors["chestplate"], leggings=armors["leggings"], boots=armors["boots"],
                   inventory=[potions["health_potion"], potions["strength_potion"]])

,"mage" : Character("Mage", 70, 5,
                main_hand=weapons["magic_staff"], off_hand=weapons["spell_book"],
                helmet=armors["helmet"], chestplate=armors["chestplate"], leggings=armors["leggings"], boots=armors["boots"],
                inventory=[potions["mana_potion"], potions["health_potion"]])

,"archer" : Character("Archer", 80, 7,
                  main_hand=weapons["wooden_bow"], off_hand=weapons["wooden_trap"],
                  helmet=armors["helmet"], chestplate=armors["chestplate"], leggings=armors["leggings"], boots=armors["boots"],
                  inventory=[potions["health_potion"]])

,"easteregg" : Character("Secret", 999, 999,
                     main_hand=weapons["basic_sword"], off_hand=weapons["basic_shield"],
                     helmet=armors["helmet"], chestplate=armors["chestplate"], leggings=armors["leggings"], boots=armors["boots"])
    
    
}


class Enemy(Entity):
    def __init__(self, name, health, strength, main_hand:Weapon=None, off_hand:Weapon=None,
                 helmet:Armor=None, chestplate:Armor=None, leggings:Armor=None, boots:Armor=None, level=1, base_xp=0,loot_table=None):
        super().__init__(name, health, strength, main_hand, off_hand,
                        helmet, chestplate, leggings, boots ,level=level, base_xp=base_xp)
        
        self.loot_table = loot_table if loot_table is not None else {}
        
        
enemies = {
"gobelin" : Enemy("Gobelin", 45, 5, main_hand=weapons["poignard"], level=1, base_xp=5,loot_table={
                      "health_potion": 25,
                      "tissu_abime": 50 
                  })
,"orque" : Enemy("Orque", 70, 15, main_hand=weapons["gourdin"], off_hand=weapons["basic_shield"], level=1, base_xp=15,loot_table={
                      "health_potion": 50,
                      "dent_orque": 4  
                  })
,"troll" : Enemy("Troll", 120, 30,
             main_hand=weapons["axe"], off_hand=weapons["basic_shield"],
             helmet=armors["helmet"], chestplate=armors["chestplate"],
             leggings=armors["leggings"], boots=armors["boots"], level=1, base_xp=45, loot_table={
                 "defenses": 30,
                 "ceinture": 10,
                 "os": 80
                 
             })
}
 