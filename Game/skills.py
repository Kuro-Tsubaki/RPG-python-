from Game.fight_manager import get_dice_result
class Skill:
    def __init__(self,name,mana_cost,power,learn_difficulty = 10,description=""):
        self.name = name
        self.mana_cost = mana_cost
        self.power = power
        self.learn_difficulty = learn_difficulty
        self.description = description
        
class DamageSkill(Skill):
    def __init__(self, name, mana_cost, power, description=""):
        super().__init__(name,mana_cost,power, description)   
        
    def cast(caster,target):
        caster.mana -= self.mana_cost
        result = get_dice_result() 
        if result == 1:
            
            caster.health -= caster.self.power
            caster.
        if result == 20:
            power *= 2
            
class SupportSkill(Skill):
    def __init__(self, name, mana_cost, power, description=""):
        super().__init__(name,mana_cost,power, description)