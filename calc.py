import random


class Pokemon:
    def __init__(self, attack:int, defence:int, power:int, level:int):
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
    
    return base_damage * random_modifier

def main():
    bob = Pokemon(20, 10, 10, 7)
    dan = Pokemon(15, 5, 15, 7)
    
    for i in range(10):

        print("damage of bob attacking dan", calculate_damage(bob, dan, True))


if __name__ == "__main__":
    main()