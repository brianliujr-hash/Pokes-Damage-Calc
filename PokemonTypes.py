from enum import Enum


class PokemonType(Enum):
    NORMAL = 1
    FIRE = 2
    WATER = 3
    ELECTRIC = 4
    GRASS = 5
    
    
super_effective_against = {
    PokemonType.NORMAL: [],
    PokemonType.FIRE: [PokemonType.GRASS],
    PokemonType.WATER: [PokemonType.FIRE],
    PokemonType.ELECTRIC: [PokemonType.WATER],
    PokemonType.GRASS: [PokemonType.WATER]
}

not_effective_against = {
    PokemonType.NORMAL: [],
    PokemonType.FIRE: [PokemonType.FIRE, PokemonType.WATER],
    PokemonType.WATER: [PokemonType.WATER, PokemonType.GRASS],
    PokemonType.ELECTRIC: [PokemonType.ELECTRIC, PokemonType.GRASS],
    PokemonType.GRASS: [PokemonType.FIRE, PokemonType.GRASS]
}

def get_effectiveness(attack_type:PokemonType, defend_type:PokemonType):
    if defend_type in super_effective_against[attack_type]:
        return 2.0
    if defend_type in not_effective_against[attack_type]:
        return 0.5
    
    return 1.0