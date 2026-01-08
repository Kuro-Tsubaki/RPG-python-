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

def scale_enemy(enemy, target_level):
    
    levels_gained = target_level - enemy.level
    
    if levels_gained > 0:
        # Calculs
        hp_scaling = levels_gained * HP_MULTIPLIER
        str_scaling = levels_gained * STR_MULTIPLIER
        
        # Application
        enemy.max_health += hp_scaling
        enemy.health = enemy.max_health # Soin complet lors du scaling
        enemy.strength += str_scaling
        enemy.level = target_level
        
        return hp_scaling, str_scaling
    return 0, 0    
    
def generate_random_enemy(player_level):
    # 1. Préparation des données
    weights = get_weights_for_level(player_level)
    enemy_key = random.choices(list(weights.keys()), weights=list(weights.values()), k=1)[0]
    target_level = get_enemy_actual_level(player_level)
    
    # 2. Création de la copie
    new_enemy = copy.deepcopy(enemies[enemy_key])
    
    # 3. Application du scaling (On appelle notre "sous-chef")
    hp_plus, str_plus = scale_enemy(new_enemy, target_level)
    
    if hp_plus > 0:
        print(f"-> {new_enemy.name} (Niv {target_level}) : +{hp_plus} HP, +{str_plus} STR")
        
    return new_enemy

    