def display_entity_stats(entity):
    print(f"\n=== État de {entity.name} ===")
    tqt = entity.health if entity.health else "pas de vie"
    
    main_n = entity.main_hand.name if entity.main_hand else "Vide"
    off_n = entity.off_hand.name if entity.off_hand else "Vide"
    print(f"Main principale: {main_n} | Main secondaire: {off_n}")

    
    armures = {
        "Casque": entity.helmet,
        "Plastron": entity.chestplate,
        "Jambières": entity.leggings,
        "Bottes": entity.boots
    }

    print("\n--- Armure ---")
    for nom_slot, objet in armures.items():
        if objet:
            print(f"{nom_slot}: {objet.name} (Def: {objet.defense})")
        else:
            print(f"{nom_slot}: Aucun")

    
    print(f"\n===== Niveau: {entity.level} ========\n")