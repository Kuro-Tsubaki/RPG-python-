

class Item:
    def __init__(self, name, stat_to_fix=None,rarity=100,value = 0, description=""):
        self.name = name
        self.description = description
        self.stat_to_fix = stat_to_fix
        self.value = value
        self.rarity = rarity
        
class Weapon(Item):
    def __init__(self, name, attack, value = 0,description=""):
        super().__init__(name, description,rarity=100)
        self.attack = attack
        self.value = value
        self.rarity = 100
# --- Weapons ---
weapons = {
"basic_sword" : Weapon("Épée Basique", 10,4, "Une épée simple mais efficace") #name, atk, gold, descr
,"basic_shield" : Weapon("Bouclier Basique", 5, 4, "Un bouclier en bois renforcé")
,"magic_staff" : Weapon("Bâton Magique", 15, 4, "Un bâton imprégné de magie")
,"spell_book" : Weapon("Grimoire", 10, 4,"Un livre de sorts anciens")
,"wooden_bow" : Weapon("Arc en Bois", 12, 4,"Un arc léger et précis")
,"wooden_trap" : Weapon("Piège en Bois", 8, 4,"Un piège artisanal")
,"poignard" : Weapon("Poignard", 10, 5,"Une lame courte et rapide")
,"gourdin" : Weapon("Gourdin", 20, 8,"Une massue lourde et brutale")
,"axe" : Weapon("Hache", 25, 10,"Une hache de guerre imposante")

}

class Loot(Item):
    def __init__(self, name, value = 0, description=""):
        super().__init__(name=name, stat_to_fix=None, value=value, description=description, rarity=100)
        self.value = value
        self.rarity = 100
loot = {
        "tissu_abime": Loot("Tissu abîmé", 2, "Un vieux morceau de tissu sale."),
        "dent_orque": Loot("Dent d'Orque", 10, "Une dent jaune et solide.")
        
        
    }
    
    

class Armor(Item):
    def __init__(self, name, defense, value = 0,description=""):
        super().__init__(name, description,rarity=100)
        self.defense = defense
        self.value = value
        self.rarity = 100
    
# --- Armors ---
armors = {
"helmet" : Armor("Casque", 5, 2,"Protection pour la tête") #name, def, gold, descr
,"chestplate" : Armor("Plastron", 15, 5, "Armure de torse robuste")
,"leggings" : Armor("Jambières", 10, 4, "Protection pour les jambes")
,"boots" : Armor("Bottes", 7, 3,"Bottes renforcées") 
    
    
}


class UseableItem(Item):
    def __init__(self, name, effect, stat_to_fix, description="", value=0):
        super().__init__(name=name, stat_to_fix=stat_to_fix, value=value, description=description, rarity=100)
        self.effect = effect
        self.value  = value
        self.rarity = 100
        
# --- Useable Item ---
potions = {
"health_potion" : UseableItem("Potion de Santé", 25 , "health", "Restaure 25 points de vie", 5)
,"strength_potion" : UseableItem("Potion de Force", 5 , "strength","Augmente la force de 5 points pour le combat en cours", 8)
,"mana_potion" : UseableItem("potion de mana" ,10 , "mana","Redonne du mana", 3)
,"luck_potion" : UseableItem("Potion d'amélioration de chance", 30,"luck", "Augmente la chance", 10)
    
}

all_items = {**weapons, **armors, **potions, **loot}