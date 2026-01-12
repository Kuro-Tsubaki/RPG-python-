from Game.character import Entity, Character
import random 
def fight(striker:Entity, defender:Entity):
    
    # ======================== #
    # === Case - Attaque === #
    # ======================== #
    
    
    brut_damage = striker.strength
    attack_display =  striker.name + " inflige  *totdamage*  damage \n"  + " "+str(striker.strength) + " force brut \n"
    #Replace *totdomage* p/ tout ce que possède le striker qui a de la force
    
    if striker.main_hand:
        brut_damage += striker.main_hand.attack
        attack_display += " " + str(striker.main_hand.attack) + " force main principale \n"
    if striker.off_hand:
        brut_damage += striker.off_hand.attack
        attack_display += " " + str(striker.off_hand.attack) + " force main secondaire \n"
    
    # ----------------
    # Dice roll DnD
    # ----------------
    
    dice_roll = random.randint(1, 20)
    print(f"\n🎲 Jet de dé :{dice_roll}\n")
    
    if dice_roll == 20:
        brut_damage *= 2
        print("🔥 Succès critique ! Attaque x2")
    if dice_roll == 1:
        brut_damage /= 2
        print("💀 Échec critique ! Attaque /2")
    
    variation = random.uniform(0.85, 1.15)
    brut_damage *= variation
    
    
    # --------
    # Mastery
    # --------
    
    if isinstance(striker, Character) and isinstance(defender, Entity):
        
        kill_count = striker.bestiary.get(defender.name, 0)
        
        if kill_count >= 40:
            brut_damage *= 3  # Bonus x3 (pour un 3-shot rapide)
            print("💥 COUP DE GRÂCE : Maîtrise Totale !")
            
        elif kill_count >= 20:
            brut_damage *= 1.5 # Bonus x1.5
            print("⚔️ Bonus de Maîtrise : +50% Dégâts.")
            
            
    brut_damage = max(1,int(brut_damage))        
    
    # ===================== #
    # ===== Defense ===== #
    # ===================== #
    
    defender_defense = 0
    defense_display = ""
    #defense_display = defender.name + "\nPossède #totdef# de defense \n" + str(defender_defense) #print du totdef defender
    
    if defender.helmet:
        defender_defense += defender.helmet.defense
        defense_display +=  " Defense " + str(defender.helmet.defense) + " " + defender.helmet.name + "\n"
    if defender.chestplate:
        defender_defense += defender.chestplate.defense
        defense_display += " Defense " + str(defender.chestplate.defense) + " " + defender.chestplate.name + "\n"
    if defender.leggings:
        defender_defense += defender.leggings.defense
        defense_display += " Defense " + str(defender.leggings.defense) + " " + defender.leggings.name + "\n"    
    if defender.boots:
        defender_defense += defender.boots.defense
        defense_display += " Defense " + str(defender.boots.defense) +  " " + defender.boots.name + "\n"
    #Ajout de la défense si en possède + affichage de chaque piece séparément ligne ??
        
        
        
    if defender_defense > 0:
        dizaines = defender_defense //10
        reduction = (dizaines / 0.7) /100 #changer le 0.7 pour équilibrage (> = plus facile. < = plus dur)
        reduction = min(reduction, 0.35) #plafond à 35% de reduction
        # =========================================== #
        defense_display += "\n Réduction: " + str(round(reduction * 100, 1)) + "%\n" #affichage reduction % selon l'armure   
    else:
        reduction = 0
        defense_display += " Aucune armure équipée\n\n"
        
        
    # === CALCUL DES DÉGÂTS FINAUX ===
    final_damage = int(brut_damage * (1 - reduction))
    final_damage = max(final_damage, 1)  # Minimum 1 dégât
    
    
    # === APPLICATION DES DÉGÂTS ===
    defender.health -= final_damage
    if defender.health < 0:
        defender.health = 0

        
        
    # ======================== #
    # === Case - Affichage === #
    # ======================== #
    
    #defense_display = defense_display.replace("#totdef#", str(defender_defense)) #ligne 15 ça sera pour dire "reduit l'attaque de % thx to /tant de defense/"
    print(str(defender.name) + " a une defense de "+ str(defender_defense) +"\n")
    print(defense_display) 
    #======================#
    attack_display = attack_display.replace("*totdamage*", str(brut_damage)) #ligne 10
    print(attack_display)
    #======================#
    print("\n-------------------------\n",defender.name, ":", defender.health, "/", defender.max_health,"HP","\n-------------------------")
    #======================#
    
def handle_victory(player,enemy):
        
        print(f"vous avez vaincu ",enemy.name, "!")   
        xp_gagne = player.calculate_experience_gain(enemy)
        player.bestiary[enemy.name] = player.bestiary.get(enemy.name, 0) + 1
        print(f"Progression : {player.bestiary[enemy.name]} {enemy.name}s vaincus.")
        player.health = player.max_health 