import random
import copy
from Game.character import enemies # Assurez-vous d'importer le dictionnaire 'enemies'

#scaling level
HP_MULTIPLIER = 5
STR_MULTIPLIER = 3


# 1. La Configuration des Poids
ENEMY_POOL_CONFIG = {
    3: { "gobelin": 80, "orque": 20, "troll": 0 }, 
    6: { "gobelin": 15, "orque": 65, "troll": 20 },
    999: { "gobelin": 5, "orque": 25, "troll": 70 }
}

def get_weights_for_level(player_level):
    # On trie pour être sûr de l'ordre des paliers
    paliers = sorted(ENEMY_POOL_CONFIG.keys())
    for p in paliers:
        if player_level <= p:
            return ENEMY_POOL_CONFIG[p]
    # Si on dépasse le max, on renvoie le dernier
    return ENEMY_POOL_CONFIG[paliers[-1]]

# Create random enemy difficulty level
def get_enemy_actual_level(player_level):
    
    roll = random.random()
    
    # 20% luck : Trash mob
    if roll < 0.20 and player_level >=3:
        low = int(player_level * 0.4)
        high = int(player_level * 0.7) +1
        level = random.randint(max(1,low),max(1,high))
        print("-> Rencontre : Ennemi Facile (Trash Mob).")

    # 70% luck : normal mob
    elif roll < 0.90:
        min_level_normal = max(1, player_level - 2) 
        level = random.randint(min_level_normal, player_level)
        print("-> Rencontre : Ennemi Standard.")

    # 10% luck : Elite mob
    else:
        level_bonus = random.randint(1, 5) 
        level = player_level + level_bonus
        print(f"-> Attention ! Rencontre : Ennemi ÉLITE (Niv +{level_bonus})!")

    return max(1, level) #security

# 2. La Fonction d'Apparition (Modifiée)
# NOTE: Cette fonction doit prendre le 'player_level' en argument, 
# car elle ne fera plus partie de la classe Game (plus de 'self').
def generate_random_enemy(player_level):
    # 1. On récupère les poids via notre nouvelle fonction propre
    current_weights = get_weights_for_level(player_level)
    
    # 2. Tirage de l'espèce (très court !)
    enemy_key = random.choices(list(current_weights.keys()), weights=list(current_weights.values()), k=1)[0]
    
    # 3.1 || scaling dynamique || Appel de la fonction get_enemy_actual_level
    enemy_actual_level = get_enemy_actual_level(player_level)
    
    # 3.2 Instance de "enemy_actual_level"
    # Création de l'enemy qu'on va affronter, après avoir scale
    enemy_instance = copy.deepcopy(enemies[enemy_key])
    
    # 3.3 Calcul de la différence de niveau entre instance et niveau du modèle basique (level=1)
    levels_gained = enemy_actual_level - enemy_instance.level
    
    # Étape 3.4 : Appliquer le Scaling si l'ennemi est d'un niveau supérieur au modèle
    if levels_gained > 0:
        
        # Scaling des PV
        hp_scaling = levels_gained * HP_MULTIPLIER
        enemy_instance.max_health += hp_scaling
        enemy_instance.health += hp_scaling # Important : PV actuels aussi !
        
        # Scaling de la Force
        strength_scaling = levels_gained * STR_MULTIPLIER
        enemy_instance.strength += strength_scaling
        
        print(f"-> {enemy_instance.name} ajusté au Niveau {enemy_actual_level}: HP +{hp_scaling}, Force +{strength_scaling}")

    # Étape 3.5 : Finaliser le niveau de l'instance
    # Même si levels_gained était 0, l'instance doit avoir le bon niveau affiché.
    enemy_instance.level = enemy_actual_level
    
    # 4. Retourner la copie de l'ennemi
    return enemy_instance

    