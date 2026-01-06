

class Item:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
#-------------------------------------------------
# Les armes héritent d'Item et ajoutent des stats d'attaque
#-------------------------------------------------
class Weapon(Item):
    def __init__(self, name, attack, description=""):
        super().__init__(name, description)
        self.attack = attack
        
# --- Armes ---
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
    
    
    
    
}

# Les armures héritent d'Item et ajoutent des stats de défense
#-------------------------------------------------
# les armures héritent d'Item et ajoutent des stats de défense
#-------------------------------------------------
class Armor(Item):
    def __init__(self, name, defense, description=""):
        super().__init__(name, description)
        self.defense = defense

    
# --- Armures ---
armors = {
"helmet" : Armor("Casque", 5, "Protection pour la tête")
,"chestplate" : Armor("Plastron", 15,  "Armure de torse robuste")
,"leggings" : Armor("Jambières", 10,  "Protection pour les jambes")
,"boots" : Armor("Bottes", 7, "Bottes renforcées") 
    
    
}


#-------------------------------------------------
# Les objets utilisables héritent d'Item et ajoutent des effets
#-------------------------------------------------
class UseableItem(Item):
    def __init__(self, name, effect, description=""):
        super().__init__(name, description)
        self.effect = effect
        
# --- Objets Utilisables ---
potions = {
"health_potion" : UseableItem("Potion de Santé", 25 , "Restaure 25 points de vie")
,"strenght_potion" : UseableItem("Potion de Force", 5 , "Augmente la force de 5 points pour le combat en cours")
,"mana_potion" : UseableItem("potion de mana" ,10 , "Redonne du mana")
    
}

