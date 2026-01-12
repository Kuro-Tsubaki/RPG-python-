def display_entity_stats(entity):
    print(f"\n=== État de {entity.name} ===")
    
    pourcentage = (entity.health / entity.max_health) * 100
    
    nb_carres = int(pourcentage / 10)
    barre = "█" * nb_carres + "░" * (10 - nb_carres)
    
    print(f"\n🫀 Santé : [{barre}] {int(pourcentage)}% ({entity.health}/{entity.max_health}) \n")
    
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

    
    print(f"\n===== Niveau: {entity.level} {'(XP: ' + str(entity.xp) + '/' + str(entity.max_xp) + ')' if hasattr(entity, 'xp') else ''} ========\n")