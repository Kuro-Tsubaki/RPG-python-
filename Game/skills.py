from Game.fight_manager import get_dice_result

ELEMENTAL_REACTION = {
    "fire" : {
        "ice": {"multiplier": 1.2, "message": "CHOC TERMIQUE !"}
        },
    "ice" :{
        "lightning": {"multiplier": 1.5, "message": "SUPERCONDUCTION !"}
    }
}

class Skill:
    def __init__(self,name,mana_cost,power,learn_difficulty = 10,description="",element = None):
        self.name = name
        self.mana_cost = mana_cost
        self.power = power
        self.learn_difficulty = learn_difficulty
        self.description = description
        self.element = element
        
class DamageSkill(Skill):
    def __init__(self, name, mana_cost, power, description="", element=None):
        super().__init__(name, mana_cost, power, description, element)   
        
    def cast(self,caster,target):
        caster.mana -= self.mana_cost
        result = get_dice_result()
        final_damage = round(result * (caster.magic_power + self.power))
        if result == 0.5: #fail
            caster.health -= final_damage
        elif result == 2: #crit
            target.health -= final_damage
        else: #(2,19)
            target.health -= final_damage
        if self.element is not None:
            target.status_effects[self.element] = True
        return True, final_damage



            
            
class SupportSkill(Skill):
    def __init__(self, name, mana_cost, power, description="",element=""):
        super().__init__(name,mana_cost,power, description,element)
        
    def cast_support(self,caster):
        caster.mana -=self.mana_cost
        result = get_dice_result()
        heal = round((caster.magic_power + self.power) * result)
        caster.health = min(caster.health + heal,caster.max_health)
        return True, heal
        

spells_list = {
    "fireball": DamageSkill("Boule de feu", 15, 13, "Lance une boule de feu qui applique debuff : 'chaud' ",element="fire")
    ,"snowball": DamageSkill("Boule de neige", 5,3,"Boule de neige qui applique debuff : 'froid'", element="ice") #later feature : slow/reduce accuracy
    ,"heal": SupportSkill("Soin minime",10,7,"Petit pansement")
 
}


