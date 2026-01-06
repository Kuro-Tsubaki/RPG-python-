# Affichage de l'équipement



def display_equipment(selected_character):
    print("\n=== Équipement ===")
    if selected_character.main_hand:
        print(f"Main principale: {selected_character.main_hand.name} (Attaque: {selected_character.main_hand.attack})")
    if selected_character.off_hand:
        print(f"Main secondaire: {selected_character.off_hand.name} (Attaque: {selected_character.off_hand.attack})")
    
    print("\n=== Armure ===")
    if selected_character.helmet:
        print(f"Casque: {selected_character.helmet.name} (Défense: {selected_character.helmet.defense})")
    if selected_character.chestplate:
        print(f"Plastron: {selected_character.chestplate.name} (Défense: {selected_character.chestplate.defense})")
    if selected_character.leggings:
        print(f"Jambières: {selected_character.leggings.name} (Défense: {selected_character.leggings.defense})")
    if selected_character.boots:
        print(f"Bottes: {selected_character.boots.name} (Défense: {selected_character.boots.defense})")
        
    print("\n=== Objets Utilisables ===")
    for item in selected_character.inventory:
        print(f"Objet utilisable: {item.name} (Effet: {item.effect}) (Description: {item.description})")
        
    print(f"\n=====Niveau: {selected_character.level}========")


def display_equipement_enemy(enemy):
    print("\n=== Équipement Ennemi ===")
    if enemy.main_hand:
        print(f"Main principale: {enemy.main_hand.name} (Attaque: {enemy.main_hand.attack})")
    if enemy.off_hand:
        print(f"Main secondaire: {enemy.off_hand.name} (Attaque: {enemy.off_hand.attack})")
    
    print("\n=== Armure Ennemi ===")
    if enemy.helmet:
        print(f"Casque: {enemy.helmet.name} (Défense: {enemy.helmet.defense})")
    if enemy.chestplate:
        print(f"Plastron: {enemy.chestplate.name} (Défense: {enemy.chestplate.defense})")
    if enemy.leggings:
        print(f"Jambières: {enemy.leggings.name} (Défense: {enemy.leggings.defense})")
    if enemy.boots:
        print(f"Bottes: {enemy.boots.name} (Défense: {enemy.boots.defense})")
    
    print(f"\n=====Niveau: {enemy.level}========")