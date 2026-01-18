# 🎮 Game Development Log  
**Date:** 09/01/2026  
**Version:** 0.1 Alpha

---

## 📈 Changelog

| Version | Date       | Changes |
|---------|------------|---------|
| **0.1** | 09/01/2026 | ✅ **Initial systems**: `fight_manager`, `useable_item`, `random_enemy` (weighted), `save_system` |
| **0.1.2** | 11/01/2026 |🪰 **Added**: Dictionnary with buff that clear when fight's over, not optimized, and corrected a bug with potions when drank.|
| **0.1.2.5** | 12/01/2026 |📦🏭 **clear code** : game.py was a trash, it's cleared but not clearest, not really an update. UX better but I will improve it later.|
| **0.1.3** | 13/01/2026 | 🛒 **Shop created**: optimized a little and unoptimized newest added code... Shop created with selling system but not market. Market on 0.1.4|
| **0.1.4** | 14/01/2025 🛒 **Shop almost finished**: miss the refresh shop and on other low fonctionality|
| **0.2** | ⏳ WIP     | 🔄 **To implement**: Shop, Skills/Buffs/Debuffs, Turn-based, Team, Dungeons |


## 🗓️ TO DO (0.2 Sprint)

- [ ] 🏪 **Shop system** — Random item generation (value + rarity) 
- [x] 🧳 **looting system** - Get loot when mobs get killed (random) 
- [ ] ⚔️ **Skills, Buffs & Debuffs** — Data structure & effects 
- [ ] 🔄 **Turn-based combat** — Core logic implementation  
- [ ] 🧑‍🤝‍🧑 **Team system** — Multi-player team formation  
- [ ] 🏰 **Dungeons** — Procedural generation enemy will attack the least armor character
- [ ] ⚖️ **Balance** - Entites to make fight balanced

---

## ⚙️ TO OPTIMISE

- **File :** `game.py`
- **File :** `save.py`
  - [ ] 💾 **Save system** — Performance optimization & structure refactor
---
- **Weapons :** `Main and off hand` player could equip 2 main weapon, instead of one per emplacement + Shield for exemple should add defense, not atk
---

### 🧠 Notes & Ideas

> **Skills :** Skill data structure 

> **Fighting journaling** History event

> **Job and tree talent** Job >> unique items
 
> **tree talent :**  Tree talent.


## 🛠️ Tech Stack
- **Language:** Python 3.13
- **Dependencies:** [random, copy]
- **Architecture:** [OOP]

