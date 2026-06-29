import random
import os
import copy

from PokemonTypes import PokemonType, get_effectiveness, super_effective_against, not_effective_against
from pokemon import Pokemon, Attack
from pokemon import load_pokemon

import fields
from fields import Field
    

def calculate_damage(attacker:Pokemon, defender:Pokemon, critical:bool, field:Field):

    critical_mod = 2 if critical else 1
    
    used_attack = attacker.get_current_attack()
    
    same_type_bonus = 1.5 if attacker.type == used_attack.type else 1.0
    
    level_and_crit_mod = (2 * attacker.level * critical_mod / 5) + 2
    
    a_div_d = attacker.attack / defender.defence
    
    random_modifier = random.randint(85, 100) / 100
    
    base_damage = (level_and_crit_mod * used_attack.power * a_div_d / 50) + 2
    
    type_effectiveness_modifier = get_effectiveness(attacker.type, defender.type)
    
    field_modifier = field.calculate_modifier(attacker)
    
    return round(base_damage * random_modifier * type_effectiveness_modifier * same_type_bonus, 1)

def list_all_pokemon(pokemon:list[Pokemon]):
    print("All pokemon:")
    
    for i, mon in enumerate(pokemon):
        print(i, mon)
        
    print("=============================================================================")
    
    
def choose_pokemon(pokemon:list[Pokemon], player_num:int) -> Pokemon:
    
    print(f"<PLAYER {player_num}>")
    
    while True:
        try:
            choice = int(input("Choose a Pokemon: "))
            if choice < 0:
                raise IndexError("Not allowing negative choices")
            return copy.deepcopy(pokemon[choice])
        except IndexError:
            print("Not a valid pokemon, try again")
        except ValueError:
            print("Not a valid number, try again")

def select_attack(pokemon:Pokemon):
    pokemon.list_moves()
 
    while True:
        try:
            choice = int(input("Choose a pokemon move: "))
            pokemon.select_attack(choice)
            return
        except ValueError:
            print("Invalid input, try again")

def battle(player1:Pokemon, player2:Pokemon) -> int:
    """
    Returns who wins the battle 
    """
    turn = random.randint(1,2)
    field = Field.create()
    print("============== BATTLE ===================")
    print(f"Field conditions: The terrain is {field.terrain} and the weather is {field.weather}!")
    print(f"Player {turn} you go first!")
    
    
    while player1.hp > 0 and player2.hp > 0:
        
        print("Player1")
        player1.list_stats()
        print("Player2")
        player2.list_stats()
              
        if turn == 1:
            attacker = player1
            defender = player2
        else:
            attacker = player2
            defender = player1
        
        # select attack
        
        print(f"Player {turn} select your attack")
        select_attack(attacker)
        
        # make damage
        
        attack = attacker.get_current_attack()
        attack_type = attack.type
        defend_type = defender.type
        
        
        critical = random.random() > 0.9
        print(f"{attacker.name} used {attacker.get_current_attack().name}!")
        damage = calculate_damage(attacker, defender, critical, field)
        if critical:
            print("It was a critical hit!")
        if defend_type in super_effective_against[attack_type]:
            print("It was super effective!")
        if defend_type in not_effective_against[attack_type]:
            print("It was not very effective!")
        
        # take hp
        
        defender.damage(damage)
        print(f"{defender.name} took {round(damage)} damage")
        
        # next turn
        
        turn = 1 if turn == 2 else 2
        
        print(f"")
        
    if player1.hp <= 0:
        return 1 
    else:
        return 2 
        
        
    

    
    
# def choose_pokemon(pokemon:list[Pokemon], player_num:int) -> Pokemon:
#     print(f"<PLAYER {player_num}")
    
#     while True:
#         choice = input("Choose a pokemon (or 'random'): ")
#         if choice.lower() == "random":
#             return choose_random_pokemon(pokemon)
#         try:
#             choice_num = int(choice)
#             if choice_num < 0 or choice_num >= len(pokemon):
#                 raise IndexError("Invalid pokemon index")
#             return copy.deepcopy(pokemon[choice_num])
#         except ValueError:
#             print("Invalid input. Enter a number or 'random'.")
#         except IndexError:
#             print("Invalid pokemon index. Please try again.")

            
def choose_random_pokemon(pokemon:list[Pokemon]) -> Pokemon:
    
    return copy.deepcopy(random.choice(pokemon))
    
    
def main():
    os.system("cls")
    
    pokemon = load_pokemon("pokemon.yml")
        
    list_all_pokemon(pokemon)
    
    player1 = choose_random_pokemon(pokemon)
    player2 = choose_random_pokemon(pokemon)
    
    
    print("player 1, you get, ")
    print(player1)
    print("player 2, you get, ")
    print(player2)
    
    winner = battle(player1, player2)
    
    print(f"The winner is player{winner}")
        
    # bob = pokemon[0]
    # dan = pokemon[1]
    
    # bob.select_attack(1)
    # dan.select_attack(2)
    
    # for i in range(10):
    #     print("damage of bob attacking dan", calculate_damage(bob, dan, False))
    
    # tackle_attack = Attack("Tackle", PokemonType.NORMAL, 40)
    # fire_punch_attack = Attack("Fire Punch", PokemonType.FIRE, 75)
    # surf_attack = Attack("Surf", PokemonType.WATER, 90)

    # bob = Pokemon(PokemonType.WATER, 20, 10, 7, [tackle_attack, fire_punch_attack])
    # dan = Pokemon(PokemonType.NORMAL, 15, 5, 7, [tackle_attack, surf_attack])
    
    # bob.select_attack(1)
    
    # dan.select_attack(1)
    
    # for i in range(10):
    #     print("damage of bob attacking dan", calculate_damage(bob, dan, True))


if __name__ == "__main__":
    main()
    
