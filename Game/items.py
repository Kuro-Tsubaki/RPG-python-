

class Item:
    def __init__(self, name, stat_to_fix=None, description=""):
        self.name = name
        self.description = description
        self.stat_to_fix = stat_to_fix

class Weapon(Item):
    def __init__(self, name, attack, description=""):
        super().__init__(name, description)
        self.attack = attack
        
# --- Weapons ---
weapons = {
"basic_sword" : Weapon("Épée Basique", 10, "Une épée simple mais efficace")
,"basic_shield" : Weapon("Bouclier Basique", 5,  "Un bouclier en bois renforcé")
,"magic_staff" : Weapon("Bâton Magique", 15,  "Un bâton imprégné de magie")
,"spell_book" : Weapon("Grimoire", 10, "Un livre de sorts anciens")
,"wooden_bow" : Weapon("Arc en Bois", 12, "Un arc léger et précis")
,"wooden_trap" : Weapon("Piège en Bois", 8, "Un piège artisanal")
,"poignard" : Weapon("Poignard", 10, "Une lame courte et rapide")
,"gourdin" : Weapon("Gourdin", 20, "Une massue lourde et brutale")
,"axe" : Weapon("Hache", 25, "Une hache de guerre imposante")
,"yes" : Weapon("tqt", 20, "jspa") 
}

class Armor(Item):
    def __init__(self, name, defense, description=""):
        super().__init__(name, description)
        self.defense = defense

    
# --- Armors ---
armors = {
"helmet" : Armor("Casque", 5, "Protection pour la tête")
,"chestplate" : Armor("Plastron", 15,  "Armure de torse robuste")
,"leggings" : Armor("Jambières", 10,  "Protection pour les jambes")
,"boots" : Armor("Bottes", 7, "Bottes renforcées") 
    
    
}


class UseableItem(Item):
    def __init__(self, name, effect, stat_to_fix ,description=""):
        super().__init__(name, description,stat_to_fix)
        self.effect = effect
        
        
# --- Useable Item ---
potions = {
"health_potion" : UseableItem("Potion de Santé", 25 , "health", "Restaure 25 points de vie")
,"strength_potion" : UseableItem("Potion de Force", 5 , "strength","Augmente la force de 5 points pour le combat en cours")
,"mana_potion" : UseableItem("potion de mana" ,10 , "mana","Redonne du mana")
,"luck_potion" : UseableItem("Potion d'amélioration de chance", 30,"luck", "Augmente la chance")
    
}

