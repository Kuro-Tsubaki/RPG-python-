

class Item:
    def __init__(self, name,stat_to_fix=None,rarity=100,value = 0, description="",slot =""):
        self.name = name
        self.description = description
        self.stat_to_fix = stat_to_fix
        self.value = value
        self.rarity = rarity
        self.slot = slot
class Weapon(Item):
    def __init__(self, name, attack, value = 0,description="",rarity=100, slot = ""):
        super().__init__(name=name, description=description,value=value,rarity=rarity,slot=slot)
        self.attack = attack
        
        
# --- Weapons ---
weapons = {
"basic_sword" : Weapon("Épée Basique", 10,4, "Une épée simple mais efficace", 90, "main_hand") #name, atk, gold, descr
,"basic_shield" : Weapon("Bouclier Basique", 5, 4, "Un bouclier en bois renforcé",90, "off_hand")
,"magic_staff" : Weapon("Bâton Magique", 15, 4, "Un bâton imprégné de magie",90, "main_hand")
,"spell_book" : Weapon("Grimoire", 10, 4,"Un livre de sorts anciens",90, "off_hand")
,"wooden_bow" : Weapon("Arc en Bois", 12, 4,"Un arc léger et précis",90, "main_hand")
,"wooden_trap" : Weapon("Piège en Bois", 8, 4,"Un piège artisanal",90, "off_hand")
,"poignard" : Weapon("Poignard", 10, 5,"Une lame courte et rapide",90, "off_hand")
,"gourdin" : Weapon("Gourdin", 20, 8,"Une massue lourde et brutale",90, "main_hand")
,"axe" : Weapon("Hache", 25, 10,"Une hache de guerre imposante",90, "main_hand")

}

class Loot(Item):
    def __init__(self, name, value = 0, description="",rarity=100):
        super().__init__(name=name, stat_to_fix=None, value=value, description=description, rarity=rarity)
        
        
loot = {
        "tissu_abime": Loot("Tissu abîmé", 2, "Un vieux morceau de tissu sale."),
        "dent_orque": Loot("Dent d'Orque", 10, "Une dent jaune et solide."),
        "defenses": Loot("défenses de Troll", 14, "Mieux vaut ne pas se faire planter avec."),
        "ceinture": Loot("Ceinture en cuir", 20, "Une ceinture pas lavé depuis..."),
        "os": Loot("Un Os",13,"Je ne donnerai même pas ça a mon chien"),
    }
    
    

class Armor(Item):
    def __init__(self, name, defense,value = 0,description="",rarity=100, slot = ""):
        super().__init__(name=name, description=description, value=value, rarity=rarity,slot=slot)
        self.defense = defense
        
        
    
# --- Armors ---
armors = {       #name,  def,value, desc="",                rarity,slots
"helmet": Armor("Casque", 5, 2, "Protection pour la tête", 0, "helmet"),
"chestplate": Armor("Plastron", 15, 5, "Armure de torse robuste", 0, "chestplate"),
"leggings": Armor("Jambières", 10, 4, "Protection pour les jambes", 0, "leggings"),
"boots": Armor("Bottes", 7, 3, "Bottes renforcées", 0, "boots"),
"wooden_h": Armor("Casque en bois", 7, 3, "Pas très confortable", 90, "helmet")
}






class UseableItem(Item):
    def __init__(self, name, effect, stat_to_fix, description="", value=0,rarity=100):
        super().__init__(name=name, stat_to_fix=stat_to_fix, value=value, description=description,rarity=rarity)
        self.effect = effect
        
        
        
# --- Useable Item ---
potions = {
"health_potion" : UseableItem("Potion de Santé", 25 , "health", "Restaure 25 points de vie", 5,85)
,"strength_potion" : UseableItem("Potion de Force", 5 , "strength","Augmente la force de 5 points pour le combat en cours", 8,85)
,"mana_potion" : UseableItem("potion de mana" ,10 , "mana","Redonne du mana", 3,85)
,"luck_potion" : UseableItem("Potion d'amélioration de chance", 30,"luck", "Augmente la chance", 10,62)
    
}

all_items = {**weapons, **armors, **potions, **loot} 
shop_items = {**weapons, **armors, **potions} #use for the shop
"""
    1 - 100 rarity level
    
100 - 90 = basique
89 - 80 = commun
79 - 70 = peu commun
69 - 60 = rare
59 - 50 = très rare
49 - 40 = épique
39 - 30 = légendaire
29 - 20 = mythique
19 - 10 = antique
9 - 2 = divin
1 = démon
"""