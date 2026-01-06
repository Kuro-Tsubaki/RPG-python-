from Game.character import characters
from Game.fight_manager import fight
from Game.inventory import Inventory
from Game.utils import display_equipment, display_equipement_enemy
from Game.save_load import save_game, load_game, get_save_file, restore_player_data
from Game.enemy_spawner import generate_random_enemy
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
                display_equipment(self.player)
                break
            print("Choix invalide ! Veuillez entrer 1, 2 ou 3.")

    
    #Système de combat (duel)    
    def battle(self):
        print("Fonctionnalité combat:")
        display_equipment(self.player) #Affiche l'équipement du joueur
        enemy = generate_random_enemy(self.player.level) #crée un ennemi selon la fonction "generate_random_enemy"
        print(f"un {enemy.name} vous fait face de {enemy.max_health} HP")
        display_equipement_enemy(enemy) #affiche l'équipement de l'ennemi qui est apparu
        ####refonte de la fonction display_equipement####
        
        #Boucle combat continue if health > 0
        while self.player.health > 0 and enemy.health > 0 :
            #Début boucle combat choix :
            print("1- Attaquer")
            print("2- Fuir")
            combat_choice = input("Votre choix : ")
            print("\n")
            
            #1. Choix de combattre, le joueur attaque while pv > 0
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

                    #C. Affichage succès
                    print(f"Progression : {self.player.bestiary[enemy.name]} {enemy.name}s vaincus.")
                    self.player.health = self.player.max_health #vie à 100%
                    return False
                else:
                    print(f"{enemy.name} Riposte !")
                    fight(enemy,self.player)
            
                    #Choix de fuite
                    #2. PV Enemy > 0 : return boucle While
            elif combat_choice == "2":
                if random.random() < 0.5: #50% fuite de base
                    print("vous avez fuit")
                    self.player.health = self.player.max_health #vie à 100%
                    return False
                #Si fuite raté l'enemie attaque
                else:
                    print("l'ennemi vous bloque la route \n")
                    fight(enemy, self.player)                
            else:
                print("choix invalide")    
        
        if self.player.health <= 0:
            print(f"\n💀 Votre {self.player.name} a été vaincu. GAME OVER.")
            
            return True # Retourne True pour indiquer une défaite
        
        return False # Si l'ennemi est mort (déjà géré dans le break), retourne False
    
    #Menu, add shop + charger save
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
            
            #start combat, print hero/random_enemy stuff, stats
            if choice == "1":
                # Appel de la méthode corrigée. is_dead sera True ou False.
                is_dead = self.battle()
                if is_dead:
                    print("\n💀 Votre personnage est mort au combat. Retour au menu de sélection des personnages.\n")
                    self.select_character() # Retourne au menu de sélection des personnages
                    
            elif choice == "2":
                print(f"Inventaire: {self.inventory.items}")
            
            elif choice == "3":
                display_equipment(self.player)
            
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
