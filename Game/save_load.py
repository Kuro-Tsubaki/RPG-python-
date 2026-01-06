import json
import os

def get_save_file(player_name):
    """Retourne le nom du fichier de sauvegarde selon le perso."""
    return f"save_{player_name.lower()}.json"

def save_game(player, inventory):
    """Sauvegarde les données du personnage dans un fichier qui lui est propre."""
    player_data = {
        "name": player.name,
        "health": player.health,
        "max_health": player.max_health,
        "strength": player.strength,
        "level": player.level,
        "inventory": inventory.items,
        "bestiary": player.bestiary,
    }
    # Equipement du joueur
    if player.main_hand:
        player_data["main_hand"] = player.main_hand.name
    if player.off_hand:
        player_data["off_hand"] = player.off_hand.name
    if player.helmet:
        player_data["helmet"] = player.helmet.name
    if player.chestplate:
        player_data["chestplate"] = player.chestplate.name
    if player.leggings:
        player_data["leggings"] = player.leggings.name
    if player.boots:
        player_data["boots"] = player.boots.name
        
    # Le fichier porte le nom du personnage
    filename = get_save_file(player.name)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(player_data, f, indent=4, ensure_ascii=False)
    print(f"✓ Partie '{player.name}' sauvegardée dans {filename}")

def load_game(player_name):
    """Charge uniquement la sauvegarde correspondant au perso choisi."""
    filename = get_save_file(player_name)
    if not os.path.exists(filename):
        print(f"Aucune sauvegarde trouvée pour {player_name} ({filename})")
        return None
    with open(filename, "r", encoding="utf-8") as f:
        player_data = json.load(f)
    print(f"✓ Sauvegarde '{player_name}' chargée depuis {filename}")
    return player_data

def restore_player_data(player, player_data, inventory, weapons, armors):
    """Restaure les données du joueur à partir des données chargées."""
    player.health = player_data.get("health", player.health)
    player.max_health = player_data.get("max_health", player.max_health)
    player.strength = player_data.get("strength", player.strength)
    player.level = player_data.get("level", 1)
    inventory.items = player_data.get("inventory", [])
    player.bestiary = player_data.get("bestiary", {})
    
    # Restaurer l'équipement
    if "main_hand" in player_data:
        main_hand_name = player_data["main_hand"]
        for weapon in weapons.values():
            if weapon.name == main_hand_name:
                player.main_hand = weapon
                break
    if "off_hand" in player_data:
        off_hand_name = player_data["off_hand"]
        for weapon in weapons.values():
            if weapon.name == off_hand_name:
                player.off_hand = weapon
                break
    if "helmet" in player_data:
        helmet_name = player_data["helmet"]
        for armor in armors.values():
            if armor.name == helmet_name:
                player.helmet = armor
                break
    if "chestplate" in player_data:
        chestplate_name = player_data["chestplate"]
        for armor in armors.values():
            if armor.name == chestplate_name:
                player.chestplate = armor
                break
    if "leggings" in player_data:
        leggings_name = player_data["leggings"]
        for armor in armors.values():
            if armor.name == leggings_name:
                player.leggings = armor
                break
    if "boots" in player_data:
        boots_name = player_data["boots"]
        for armor in armors.values():
            if armor.name == boots_name:
                player.boots = armor
                break
    
    print(f"✓ Données du joueur {player.name} restaurées.")
