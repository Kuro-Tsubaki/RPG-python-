from Game.character import characters, Entity 
from Game.fight_manager import fight
from Game.inventory import Inventory
from Game.utils import display_entity_stats
from Game.save_load import save_game, load_game, get_save_file, restore_player_data
from Game.enemy_spawner import generate_random_enemy, get_enemy_actual_level
from Game.items import weapons, armors
import random
import copy


class Game:
    def __init__(self):
        self.player = None
        self.inventory = Inventory()
        
    #selection de la classe    
    def select_character(self):
        # Dictionnaire des personnages disponibles
        available_characters = {
            "1": characters[ "warrior"],
            "2": characters["mage"],
            "3": characters["archer"],
            "4": characters["easteregg"]
            
        }
        # Boucle de sélection du personnage
        while True:
            input_choice = input("Entrez :\n1- pour Guerrier, \n2- pour Mage, \n3- pour Archer: \nVotre choix : ")
            selected_character = available_characters.get(input_choice)
            
            if selected_character:
                self.player = copy.deepcopy(selected_character)
                # Affichage des informations du personnage sélectionné
                print(f"\nVous avez choisi: {self.player.name}")
                print(f"Santé: {self.player.health} | Force: {self.player.strength}")
                display_entity_stats(self.player)
                break
            print("Choix invalide ! Veuillez entrer 1, 2 ou 3.")

    
    #Système de combat (duel)    
    def battle(self):
        print("Fonctionnalité combat:")
        display_entity_stats(self.player)
        print(f"Vous avez {self.player.health}/{self.player.max_health} HP.") #changer display_entity_stats en mettant les hp à la place de ça
        enemy = generate_random_enemy(self.player.level)
        print(f"Un {enemy.name} de {enemy.max_health} HP vous fait face.")
        display_entity_stats(enemy)
        
        
        #Boucle combat continue if health > 0
        while self.player.health > 0 and enemy.health > 0 :
            print("1- Attaquer")
            print("2- Fuir")
            print("3- Inventaire")
            combat_choice = input("Votre choix : \n")
            
            if combat_choice == "1":
                fight(self.player, enemy)
                #2. Check PV, Si enemy.health <= 0 : break
                if enemy.health <= 0:
                    
                    #A. Victoire
                    print(f"vous avez vaincu ",enemy.name, "!")
                    # Gestion de l'expérience, du loot, etc. (à ajouter)
                    
                    #B. Système de trophée (Bestiary)
                    # Vérification
                    if enemy.name not in self.player.bestiary:
                        self.player.bestiary[enemy.name] = 0    

                    # Ajout compteur bestiary
                    self.player.bestiary[enemy.name] += 1
                    
                    #C. Def XP
                    base_xp = enemy.base_xp
                    
                    if enemy.level > self.player.level: # ELITE
                        rank_multiplier = 2.0
                        random_bonus = int(self.player.max_xp * 0.10) # 10% de l'XP max du joueur

                    elif enemy.level < int(self.player.level * 0.7): # TRASH
                        rank_multiplier = 0.6
                        random_bonus = 0

                    else: # STANDARD
                        rank_multiplier = 1.0
                        random_bonus = random.randint(1, 5)
                        
                    # 3. Calcul XP
                    total_xp = int((base_xp * rank_multiplier) + random_bonus)
                    self.player.gain_xp(total_xp)
                    
                    #D. Trophy
                    print(f"Progression : {self.player.bestiary[enemy.name]} {enemy.name}s vaincus.")
                    self.player.health = self.player.max_health 
                    break
                else:
                    print(f"{enemy.name} Riposte !")
                    fight(enemy,self.player)
            
                    
                    #2. PV Enemy > 0 : return boucle While
            elif combat_choice == "2":
                if random.random() < 0.5: #50% escape
                    print("vous avez fuit")
                    self.player.health = self.player.max_health / 2
                    break
                
                else:
                    print("l'ennemi vous bloque la route \n")
                    fight(enemy, self.player)                
            elif combat_choice == "3":
                objet_utilise = self.show_inventory()
                if objet_utilise == False:
                    continue 
            else:
                print("choix invalide")    
                
        for stat, total_bonus in self.player.active_buffs.items():
            new_stat = getattr(self.player, stat)
            base_stat = new_stat - total_bonus
            setattr(self.player, stat, base_stat)
            print(f"L'effet de {stat} se dissipe ({new_stat} -> {base_stat})")
        self.player.active_buffs.clear()
        
        if self.player.health <= 0:
            print(f"\n💀 Votre {self.player.name} a été vaincu. GAME OVER.")
            
            return True # Retourne True pour indiquer une défaite
        
        return False # Si l'ennemi est mort (déjà géré dans le break), retourne False
    def show_inventory(self):
        inventory = self.player.inventory
        
        if len(inventory) == 0:
            print("\n Votre sac est vide...\n")
            return False
        
        print("\n--- Votre inventaire ---\n")
        for i, item in enumerate(inventory):
            print(f"{i + 1}. {item.name} ({item.description})")
        print(f"{len(inventory) + 1}. Retour au menu")
        
        choice = input("\nQuel objet voulez-vous selectionner ?\n")
        if choice.isdigit():
            index = int(choice)
            if index == len(inventory)+ 1:
                return False
            index -= 1
            if index >=0 and index < len(self.player.inventory):
                selected_object = inventory[index]
                self.player.use_item(selected_object)
                return True
            else:
                print("Ce numéro n'est pas dans le sac.")
        
        else:
            print("Choix invalide, veuillez choisir un chiffre.")
        return False   


            
    def menu(self):
        self.select_character()
        
        # Boucle du menu principal
        while True:
            print("\n========== MENU PRINCIPAL ==========")
            print("1- Combattre")
            print("2- Afficher inventaire")
            print("3- Afficher équipement")
            print("4- Utiliser un consommable")
            print("5- Ouvrir le shop")
            print("6- Dongeons")
            print("7- Sauvegarder")
            print("8- Charger sauvegarde")
            print("9- Changer de personnage")
            print("10- Quitter")
            print("====================================")
            
            choice = input("Votre choix : ")
            
            if choice == "1":
                is_dead = self.battle()
                if is_dead:
                    print("\n💀 Votre personnage est mort au combat. Retour au menu de sélection des personnages.\n")
                    self.select_character()
                    
            elif choice == "2":
                self.show_inventory()
            
            elif choice == "3":
                display_entity_stats(self.player)
            
            elif choice == "4":
                pass
            
            elif choice =="5":
                pass    
            
            elif choice =="6":
                #Dongeons
                pass
                
            elif choice == "7":
                save_game(self.player, self.inventory)
            
            elif choice == "8":
                data = load_game(self.player.name)
                if data:
                    restore_player_data(self.player, data, self.inventory, weapons, armors)
                    
            elif choice == "9":
                self.select_character()
                
            elif choice == "10":
                print("Au revoir !")
                break
            
            else:
                print("Choix invalide !")
