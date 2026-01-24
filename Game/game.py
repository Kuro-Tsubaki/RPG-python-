from Game.character import characters, Entity, Mage
from Game.fight_manager import fight, handle_victory
from Game.inventory import Inventory
from Game.utils import display_entity_stats
from Game.save_load import save_game, load_game, get_save_file, restore_player_data
from Game.enemy_spawner import generate_random_enemy, get_enemy_actual_level
from Game.items import weapons, armors, shop_items, Weapon, Armor, UseableItem,Catalyst, Shield
from Game.shop_manager import Shop
from Game.skills import DamageSkill,SupportSkill
import random
import copy


class Game:
    def __init__(self,):
        self.player = None
        self.inventory = Inventory()
        self.shop = Shop()
        
    #selection de la classe    
    def select_character(self):
        # Dictionnaire des personnages disponibles
        available_characters = {
            "1": characters["warrior"],
            "2": characters["mage"],
            "3": characters["archer"]
            
        }
        # Boucle de sélection du personnage
        while True:
            input_choice = input("Entrez :\n1- pour Guerrier, \n2- pour Mage, \n3- pour Archer: \nVotre choix : ")
            selected_character = available_characters.get(input_choice)
            
            if selected_character:
                self.player = copy.deepcopy(selected_character)
                print(f"\nVous avez choisi: {self.player.name} \n Santé: {self.player.health} | Force: {self.player.strength}")
                display_entity_stats(self.player)
                break
            print("Choix invalide ! Veuillez entrer 1, 2 ou 3.")
    
    
    def battle(self):
        print("Fonctionnalité combat:")
        display_entity_stats(self.player)
        enemy = generate_random_enemy(self.player.level)
        display_entity_stats(enemy)
    
        while self.player.health > 0 and enemy.health > 0 :
            print("1- Attaquer")
            print("2- Fuir")
            print("3- Inventaire")
            print("4- Sorts")
            combat_choice = input("Votre choix : \n")
            
            if combat_choice == "1":
                fight(self.player, enemy)
                #2. Check PV, Si enemy.health <= 0 : break
                if enemy.health <= 0:
                    handle_victory(self.player,enemy)
                    self.shop.refresh_shop(self.player)
                    self.player.reroll_cost = 15
                    break
                else:
                    print(f"{enemy.name} Riposte !")
                    fight(enemy,self.player)
                    
            elif combat_choice == "2":
                if random.random() < 0.5: 
                    print("vous avez fuit")
                    self.player.health = self.player.max_health / 2
                    self.shop.refresh_shop(self.player)
                    self.player.reroll_cost = 15
                    break
                else:
                    print("l'ennemi vous bloque la route \n")
                    fight(enemy, self.player)
                    
            elif combat_choice == "3":
                objet_utilise = self.show_inventory()
                if objet_utilise == False:
                    continue
            elif combat_choice == "4":
                if self.show_skills_menu(enemy):
                    if enemy.health <=0:
                        handle_victory(self.player,enemy)
                        self.shop.refresh_shop(self.player)
                        self.player.reroll_cost = 15
                        break
                    else:
                        print(f"{enemy.name} Riposte !")
                        fight(enemy, self.player)
                
        for stat, total_bonus in self.player.active_buffs.items():
            new_stat = getattr(self.player, stat)
            base_stat = new_stat - total_bonus
            setattr(self.player, stat, base_stat)
            if self.player.health > 0:
                print(f"L'effet de {stat} se dissipe ({new_stat} -> {base_stat})")
        self.player.active_buffs.clear()
        
        if self.player.health <= 0:
            print(f"\n💀 Votre {self.player.name} a été vaincu. GAME OVER.")
            return True # True = defeat    
        return False # security if enemy dead : return False
    
    def show_inventory(self):
        inventory = self.player.inventory
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
            choice = input("\nQuel objet voulez-vous utiliser ?\n")
            if choice.isdigit():
                index = int(choice)
                if index == len(sorted_inventory) + 1:
                    return False
                index -= 1
                if 0 <= index < len(sorted_inventory):
                    selected_object = sorted_inventory[index]
                    if isinstance(selected_object,UseableItem):
                        succeed = self.player.use_item(selected_object)
                        if succeed:
                            inventory.remove(selected_object)
                            return selected_object
                    elif isinstance(selected_object,(Weapon, Armor,Shield,Catalyst)):
                        succeed = self.player.equip(selected_object)
                    else:
                        print("Cet objet n'est pas utilisatable ou équipable")
                else:
                    print("Ce numéro n'est pas dans le sac.")
            else:
                print("Choix invalide, veuillez choisir un chiffre.")
                
    def show_skills_menu(self,enemy):
        skills = self.player.skills
        checking_skills = True
        while checking_skills:
            if len(skills) == 0:
                print("\n Vous n'avez pas de sort...\n")
                return False
            if self.player.mana == 0:
                print("Vous n'avez plus de mana")
                return False

            print("\n--- Votre inventaire de sortilèges ---\n")
            sorted_spells = sorted(skills, key=lambda x: x.name)

            for i, skills in enumerate(sorted_spells):
                print(f"{i + 1}. {skills.name} | {skills.power} points de dégats| Coût: {skills.mana_cost}/{self.player.mana} mana du joueur actuel | {skills.description}")
            print(f"{len(sorted_spells) + 1}. Retour au menu")

            choice = input("\nQuel sort voulez-vous lancer ?\n")
            if choice.isdigit():
                index = int(choice)
                if index == len(sorted_spells) + 1:
                    return False
                index -= 1
                if 0 <= index < len(sorted_spells):
                    selected_skills = sorted_spells[index]
                    if not self.player.mana >= selected_skills.mana_cost:
                        print("Vous n'avez pas assez de mana")
                        return False
                    else:
                        if isinstance(selected_skills,DamageSkill):
                            shoot, damages = selected_skills.cast(self.player,enemy)
                            if shoot:
                                print(f"\n✨ {self.player.name} incante {selected_skills.name} !")
                                print(f"💥 {enemy.name} subit {damages} points de dégâts magiques.")
                                print(f"❤️ Vie restante de {enemy.name} : {enemy.health}/{enemy.max_health}")
                            return True
                        elif isinstance(selected_skills,(SupportSkill)):
                            pass #later
                        #pas besoin de else, le sort appartiendra forcément a une catégorie
                else:
                    print("Ce numéro n'est pas dans le sac.")
            else:
                print("Choix invalide, veuillez choisir un chiffre.")                        
    def menu(self):
        self.select_character()
        
        # Boucle du menu principal
        while True:
            print("\n========== MENU PRINCIPAL ==========")
            print("1- Combattre")
            print("2- Afficher inventaire")
            print("3- Afficher équipement")
            print("4- Job - en construction")
            print("5- Ouvrir le shop")
            print("6- Dongeons - en construction")
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
                self.shop.open_menu(self.player)
            
            elif choice =="6":
                #Dungeons
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
