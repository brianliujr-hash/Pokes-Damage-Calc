import random

from PokemonTypes import PokemonType, get_effectiveness

class Pokemon:
    def __init__(self, type:PokemonType, attack:int, defence:int, power:int, level:int):
        self.type = type
        self.level = level
        self.attack = attack
        self.defence = defence
        self.power = power


def calculate_damage(attacker:Pokemon, defender:Pokemon, critical:bool):

    
    critical_mod = 2 if critical else 1
    
    level_and_crit_mod = (2 * attacker.level * critical_mod / 5) + 2
    
    a_div_d = attacker.attack / defender.defence
    
    random_modifier = random.randint(85, 100) / 100
    base_damage = (level_and_crit_mod * attacker.power * a_div_d / 50) + 2
    
    type_effectiveness_modifier = get_effectiveness(attacker.type, defender.type)
    
    return base_damage * random_modifier * type_effectiveness_modifier

def main():
    bob = Pokemon(PokemonType.WATER, 20, 10, 10, 7)
    dan = Pokemon(PokemonType.NORMAL, 15, 5, 15, 7)
    for i in range(10):

        print("damage of bob attacking dan", calculate_damage(bob, dan, True))


if __name__ == "__main__":
    main()