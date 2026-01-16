from Game.character import Entity, Character
from Game.items import shop_items
import random

class Shop:
    def __init__(self):
        self.shop_slots = [None] * 4
        self.shop_locked = False
        self.reroll_cost = 15
    def select_item(self, player):
        inventory = player.inventory
        checking_inventory = True
        while checking_inventory:
            if len(inventory) == 0:
                print("\n Votre sac est vide...\n")
                return False
            print("\n--- Votre inventaire ---\n")
            sorted_inventory = sorted(inventory, key=lambda x: x.name)
            for i, item in enumerate(sorted_inventory):
                print(f"{i + 1}. {item.name} | {item.description} | Prix: {item.value}g")
            print(f"{len(sorted_inventory) + 1}. Retour au menu")
            choice = input("\nQuel objet voulez-vous selectionner ?\n")
            if choice.isdigit():
                index = int(choice)
                if index == len(sorted_inventory) + 1:
                    return False
                index -= 1
                if 0 <= index < len(sorted_inventory):
                    selected_object = sorted_inventory[index]
                    return selected_object
                else:
                    print("Ce numéro n'est pas dans le sac.")
            else:
                print("Choix invalide, veuillez choisir un chiffre.")

    def _handle_buy(self, player):
        # On ne garde que les vrais objets pour le tri
        available_items = [item for item in self.shop_slots if item is not None]
        
        if not available_items:
            print("\nL'étalage est vide !")
            return

        # Tri alphabétique
        sorted_items = sorted(available_items, key=lambda x: x.name)

        print("\n--- OBJETS À VENDRE (Triés par nom) ---")
        for i, item in enumerate(sorted_items):
            prix_achat = int(item.value * 1.4)
            print(f"{i+1}. {item.name} | Prix : {prix_achat}g")
        
        print(f"{len(sorted_items) + 1}. Retour")
        
        buy_input = input("\nQuel objet voulez-vous acheter ? ")
        if buy_input.isdigit():
            index = int(buy_input) - 1
            if index == len(sorted_items): # Retour
                return
            
            if 0 <= index < len(sorted_items):
                selected_item = sorted_items[index]
                prix_achat = int(selected_item.value * 1.4)
                
                if player.gold >= prix_achat:
                    player.gold -= prix_achat
                    player.inventory.append(selected_item)
                    
                    # On cherche l'objet dans les slots originaux pour le mettre à None
                    for i, slot in enumerate(self.shop_slots):
                        if slot == selected_item:
                            self.shop_slots[i] = None
                            break
                    print(f"Achat réussi : {selected_item.name} !")
                else:
                    print("Or insuffisant.")

    def refresh_shop(self, player):
        if self.shop_locked:
            return

        
        tiers = {
            1: 90,   # Basique
            5: 80,   # Commun
            10: 70,  # Peu commun
            15: 60,  # Rare
            20: 50,  # Très rare
            25: 40,  # Épique
            30: 30,  # Légendaire
            35: 20,  # Mythique
            40: 10,  # Antique
            45: 2,   # Divin
            50: 1,   # Démon
            
        }

        possible_items = []
        
        
        for item in shop_items.values():
            # Checking if item goes to level unlocked by the player
            for min_lvl, min_rarity in tiers.items():
                if player.level >= min_lvl and item.rarity >= min_rarity:
                    if item not in possible_items:
                        possible_items.append(item)
                        
        weights = [item.rarity for item in possible_items]
        self.shop_slots = random.choices(possible_items, weights=weights, k=4)

    def _handle_reroll(self, player):
        if player.shop_locked:
            print("Le shop est verrouillé, vous ne pouvez pas actualiser.")
            return
        if player.gold >= player.reroll_cost:
            player.gold -= player.reroll_cost
            self.refresh_shop(player)
            player.reroll_cost = int(player.reroll_cost * 1.35)
            print(f"Boutique actualisée. Prochain coût : {player.reroll_cost}g")
        else:
            print("Vous n'avez pas assez de gold.")

    def _handle_lock(self, player):
        player.shop_locked = not player.shop_locked
        status = "VERROUILLÉ" if player.shop_locked else "OUVERT"
        print(f"\n[INFO] Le shop est désormais {status}.")

    def open_menu(self, player):
        if all(slot is None for slot in self.shop_slots):
            self.refresh_shop(player)
        while True:
            lock_text = "Déverrouiller" if player.shop_locked else "Verrouiller"
            print(f"\n--- MARCHAND (Or: {player.gold}g | Reroll: {player.reroll_cost}g) ---")
            print("1- Acheter")
            print("2- Vendre")
            print("3- Actualiser")
            print(f"4- {lock_text} le shop")
            print("5- Quitter")

            shop_choice = input("Votre choix : ")

            if shop_choice == "1":
                self._handle_buy(player)
            elif shop_choice == "2":
                shop_selected_object = self.select_item(player)
                if shop_selected_object:
                    player.gold += shop_selected_object.value
                    player.inventory.remove(shop_selected_object)
                    print(f"{shop_selected_object.name} vendu pour {shop_selected_object.value}g !")
            elif shop_choice == "3":
                self._handle_reroll(player)
            elif shop_choice == "4":
                self._handle_lock(player)
            elif shop_choice == "5":
                break
            else:
                print("Choix invalide.")