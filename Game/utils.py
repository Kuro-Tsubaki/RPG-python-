def display_entity_stats(entity):
    print(f"\n=== État de {entity.name} ===")
    
    # Gestion simplifiée des mains (Ternaire : Valeur_Si_Vrai if Condition else Valeur_Si_Faux)
    main_n = entity.main_hand.name if entity.main_hand else "Vide"
    off_n = entity.off_hand.name if entity.off_hand else "Vide"
    print(f"Main principale: {main_n} | Main secondaire: {off_n}")

    # Le dictionnaire dont on a parlé
    armures = {
        "Casque": entity.helmet,
        "Plastron": entity.chestplate,
        "Jambières": entity.leggings,
        "Bottes": entity.boots
    }

    print("\n--- Armure ---")
    for nom_slot, objet in armures.items():
        if objet:
            # ICI : On ne touche à .name QUE si objet n'est pas None
            print(f"{nom_slot}: {objet.name} (Def: {objet.defense})")
        else:
            # Correction de ton bug : On n'essaie pas d'afficher .name ici
            print(f"{nom_slot}: Aucun")

    # Affichage du niveau tout en bas
    print(f"\n===== Niveau: {entity.level} ========\n")