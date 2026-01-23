from Game.items import (weapons, shields, catalysts,armors, potions, Weapon, Armor, UseableItem,Shield,Catalyst,)
import random
class Entity:
    def __init__(self, name, health, strength,magic_power,mana=100, main_hand:Weapon=None, off_hand:Weapon=None,
                 helmet:Armor=None, chestplate:Armor=None, leggings:Armor=None, boots:Armor=None, inventory:list[UseableItem]=[], level=1,xp=0, max_xp=100, base_xp=0, skills= []):
        self.name = name
        #Stat
        self.health = health
        self.max_health = health
        self.strength = strength
        self.mana = mana
        self.max_mana = mana
        self.magic_power = magic_power
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
        self.shop_locked = False
        self.reroll_cost = 15
        self.shop_slots = [None] * 4
        #---
        self.skills = skills
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
        self.max_health += 15
        self.health = self.max_health
        
        
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
        elif item.stat_to_fix == "mana":
            up_stat = min(up_stat, self.max_mana)
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
    def __init__(self, name, health, strength,magic_power,mana=100,main_hand:Weapon=None, off_hand:Weapon=None,
                 helmet:Armor=None, chestplate:Armor=None, leggings:Armor=None, boots:Armor=None, inventory=[],level=1, base_xp=0, gold = 100, skills = []):
        super().__init__(name, health, strength, magic_power,mana,main_hand, off_hand,
                        helmet, chestplate, leggings, boots, inventory,level=level, base_xp=base_xp, skills=skills)
        #others
        self.gold = gold
        #stuff
        self.equipped_weapon = None
        self.equipped_armor = None
        #stats
        self.defense = 0
        
    def level_up(self):
        super().level_up()

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
   
    def equip(self, item):
        target_slot = ""
        
        # Étape 1 : Identification du tiroir (Slot)
        if isinstance(item, (Weapon,Shield,Catalyst)):
            choix = input(f"Equiper {item.name} en : 1. Main principale / 2. Main secondaire ? ")
            target_slot = "main_hand" if choix == "1" else "off_hand"
        elif hasattr(item, 'slot') and item.slot != "":
            target_slot = item.slot # On récupère l'étiquette fixe de l'armure
            
        # Étape 2 : L'échange
        if target_slot:
            old_item = getattr(self, target_slot)
            
            if old_item:
                self.inventory.append(old_item)
                print(f"🔄 {old_item.name} retourne dans le sac.")
    
            setattr(self, target_slot, item)
            if item in self.inventory:
                self.inventory.remove(item)
            print(f"✅ {item.name} équipé en {target_slot} !")
        else:
            print(f"{item.name} n'a pas d'emplacement attitré")
            

class Warrior(Character):
    def level_up(self):
        super().level_up()
        self.strength+=2
        print(f" Force augmenté : {self.strength}")
class Mage(Character):
    def level_up(self):
        super().level_up()
        self.magic_power += 2 
        self.max_mana += 20
        self.mana = self.max_mana
        print(f" Mana Max augmenté : {self.max_mana}")
        
class Archer(Character):
    def level_up(self):
        super().level_up()
        self.strength +=2
        print(f" Force augmenté : {self.strength}")
        
characters = {
"warrior" : Warrior("Guerrier", health=100, strength=8,magic_power=0,mana=100,
                   main_hand=weapons["basic_sword"], off_hand=shields["basic_shield"],
                   helmet=armors["helmet"], chestplate=armors["chestplate"], leggings=armors["leggings"], boots=armors["boots"],
                   inventory=[potions["health_potion"], potions["strength_potion"]])

,"mage": Mage("Mage", health=70, strength=4, magic_power=12,mana=100,
                 main_hand=catalysts["magic_staff"], 
                 off_hand=catalysts["spell_book"],
                 helmet=armors["helmet"], 
                 chestplate=armors["chestplate"], 
                 leggings=armors["leggings"], 
                 boots=armors["boots"],
                 inventory=[potions["mana_potion"], potions["health_potion"]])

,"archer" : Archer("Archer", health=80, strength=9,magic_power=0,mana=100,
                  main_hand=weapons["wooden_bow"], off_hand=weapons["wooden_trap"],
                  helmet=armors["helmet"], chestplate=armors["chestplate"], leggings=armors["leggings"], boots=armors["boots"],
                  inventory=[potions["health_potion"]])

}


        
class Enemy(Entity):
    def __init__(self, name, health, strength,magic_power=0,mana=0,main_hand:Weapon=None, off_hand:Weapon=None,
                 helmet:Armor=None, chestplate:Armor=None, leggings:Armor=None, boots:Armor=None, level=1, base_xp=0,loot_table=None,skills = []):
        super().__init__(name, health, strength,magic_power,mana, main_hand, off_hand,
                        helmet, chestplate, leggings, boots ,level=level, base_xp=base_xp, skills=skills)
        
        self.loot_table = loot_table if loot_table is not None else {}
        
        
enemies = {
"gobelin" : Enemy("Gobelin", health=45, strength=5,magic_power=0,mana=0, main_hand=weapons["poignard"], level=1, base_xp=5,loot_table={
                      "health_potion": 25,
                      "tissu_abime": 50 
                  })
,"orque" : Enemy("Orque", health=70, strength=15,magic_power=0,mana=0, main_hand=weapons["gourdin"], off_hand=shields["basic_shield"], level=1, base_xp=15,loot_table={
                      "health_potion": 50,
                      "dent_orque": 4  
                  })
,"troll" : Enemy("Troll", health=120, strength=30,magic_power=0,mana=0,
             main_hand=weapons["axe"], off_hand=shields["basic_shield"],
             helmet=armors["helmet"], chestplate=armors["chestplate"],
             leggings=armors["leggings"], boots=armors["boots"], level=1, base_xp=45, loot_table={
                 "defenses": 30,
                 "ceinture": 10,
                 "os": 80
                 
             })
}
 
 
#later : enemy could use skills