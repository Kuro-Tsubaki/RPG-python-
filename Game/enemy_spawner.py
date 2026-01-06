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



# Nouvel utilitaire de génération de niveau d'ennemi
def get_enemy_actual_level(player_level):
    
    roll = random.random()
    
    # 20% de chance : Ennemi Faible
    if roll < 0.20: 
        min_level_range = int(player_level * 0.5)
        max_level_range = int(player_level * 0.7)
        #sécurité pour éviter que le chiffre soit inférieur à 1 sinon erreur
        a = max(1, min_level_range)
        b = max(1, max_level_range)
        
        level = random.randint(a,b)
        print("-> Rencontre : Ennemi Facile (Trash Mob).")

    # 70% de chance : Ennemi Normal
    elif roll < 0.90:
        min_level_normal = max(1, player_level - 2) 
        level = random.randint(min_level_normal, player_level)
        print("-> Rencontre : Ennemi Standard.")

    # 10% de chance : Ennemi Élite
    else:
        level_bonus = random.randint(1, 5) 
        level = player_level + level_bonus
        print(f"-> Attention ! Rencontre : Ennemi ÉLITE (Niv +{level_bonus})!")

    return max(1, level) # Toujours s'assurer que le niveau est au moins 1

# 2. La Fonction d'Apparition (Modifiée)
# NOTE: Cette fonction doit prendre le 'player_level' en argument, 
# car elle ne fera plus partie de la classe Game (plus de 'self').
def generate_random_enemy(player_level):
    
    current_weights_config = None
    
    # 1. Déterminer le Bon Palier
    for max_level in sorted(ENEMY_POOL_CONFIG.keys()):
        if player_level <= max_level:
            current_weights_config = ENEMY_POOL_CONFIG[max_level]
            break

    if current_weights_config is None:
        current_weights_config = ENEMY_POOL_CONFIG[max(ENEMY_POOL_CONFIG.keys())]

    # 2. Extraire les Noms et les Poids
    enemies_keys = list(current_weights_config.keys())
    weights = list(current_weights_config.values())

    # 3. Tirage Aléatoire Pondéré
    enemy_key = random.choices(enemies_keys, weights=weights, k=1)[0]

    # 3.1 || scaling dynamique || Appel de la fonction get_enemy_actual_level
    enemy_actual_level = get_enemy_actual_level(player_level)

    # Sécurité: lvl /=/ 0
    enemy_actual_level = max(1, enemy_actual_level)
    
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

    