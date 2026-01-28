import random

from PokemonTypes import PokemonType, get_effectiveness

class Attack:
    def __init__(self, name:str, type, power:int):
        self.name = name
        self.type = type
        self.power = power

class Pokemon:
    def __init__(self, type:PokemonType, attack:int, defence:int, level:int, attacks:list[Attack]):
        self.type = type
        self.level = level
        self.attack = attack
        self.defence = defence
        self.known_attacks = attacks
        self.selected_attack = 0
        
        if len(attacks) < 1:
            raise ValueError("Expected number of known attacks to be at least 1")
        
    def select_attack(self, index:int):
        if index < 1 or index >= len(self.known_attacks):
            raise ValueError(f"Selected invalid attack index {index} when only {len(self.known_attacks)} attacks known")
        
        self.selected_attack = index - 1
        
    def get_current_attack(self) -> Attack:
        return self.known_attacks[self.selected_attack]

def calculate_damage(attacker:Pokemon, defender:Pokemon, critical:bool):

    
    critical_mod = 2 if critical else 1
    
    used_attack = attacker.get_current_attack()
    
    same_type_bonus = 1.5 if attacker.type == used_attack.type else 1.0
    
    def calculate_damage(attacker:Pokemon, defender:Pokemon, critical:bool) -> float:
        same_type_bonus = 1.5 if attacker.type == used_attack.type else 1.0
    
    level_and_crit_mod = (2 * attacker.level * critical_mod / 5) + 2
    
    a_div_d = attacker.attack / defender.defence
    
    random_modifier = random.randint(85, 100) / 100
    
    base_damage = (level_and_crit_mod * used_attack.power * a_div_d / 50) + 2
    
    type_effectiveness_modifier = get_effectiveness(attacker.type, defender.type)
    
    return round(base_damage * random_modifier * type_effectiveness_modifier * same_type_bonus, 1)

def main():
    tackle_attack = Attack("Tackle", PokemonType.NORMAL, 40)
    fire_punch_attack = Attack("Fire Punch", PokemonType.FIRE, 75)
    surf_attack = Attack("Surf", PokemonType.WATER, 90)

    bob = Pokemon(PokemonType.WATER, 20, 10, 7, [tackle_attack, fire_punch_attack])
    dan = Pokemon(PokemonType.NORMAL, 15, 5, 7, [tackle_attack, surf_attack])
    
    bob.select_attack(1)
    
    dan.select_attack(1)
    
    for i in range(10):
        print("damage of bob attacking dan", calculate_damage(bob, dan, True))


if __name__ == "__main__":
    main()