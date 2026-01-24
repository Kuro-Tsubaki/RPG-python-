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
        return True, final_damage
        
            
            
class SupportSkill(Skill):
    def __init__(self, name, mana_cost, power, description=""):
        super().__init__(name,mana_cost,power, description)
        
    def cast_support(self,caster,target):
        caster.mana -=self.mana_cost
        result = get_dice_result()
        #has attr support : getattr sort,heal.... getattr sort,shield... getattr sort,enhance

spells_list = {
    "fireball": DamageSkill("Boule de feu", 15, 13, "Lance une boule de feu qui explose à l'impact")
    ,"snowball": DamageSkill("Boule de neige", 5,3,"Boule de neige qui applique debuff : 'froid'") #later feature : slow/reduce accuracy
    
 
}


