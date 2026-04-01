import yaml

from PokemonTypes import PokemonType
from yaml import Loader



class Attack:
    def __init__(self, name:str, type, power:int):
        self.name = name
        self.type = type
        self.power = power
        
    def __str__(self) -> str:
        return f"[Attack] {self.name} type= {self.type.name} power: {self.power}"

class Pokemon:
    def __init__(self, name:str, type:PokemonType, attack:int, defence:int, level:int, attacks:list[Attack], hp:float):
        self.name = name 
        self.type = type
        self.level = level
        self.attack = attack
        self.defence = defence
        self.known_attacks = attacks
        self.selected_attack = 0
        self.hp = hp
        self.max_hp = hp
        
        if len(attacks) < 1:
            raise ValueError("Expected number of known attacks to be at least 1")
        
    def select_attack(self, index:int):
        if index < 1 or index > len(self.known_attacks):
            raise ValueError(f"Selected invalid attack index {index} when only {len(self.known_attacks)} attacks known")
        
        self.selected_attack = index - 1
        
    def get_current_attack(self) -> Attack:
        return self.known_attacks[self.selected_attack]
    
    def damage(self,amount:float):
        self.hp -= round(amount)
    
    def list_moves(self):
        print(f"{self.name}'s known attacks")
        for i, move in enumerate(self.known_attacks):
            print(f"{i + 1}, {move.name}")
            
    def list_stats(self):
        print(f"{self.name} {self.hp}/{self.max_hp} {self.attack} {self.defence}")
    
    def __str__(self) -> str:
        out = f"Pokemon: name: {self.name} level: {self.level} hp: {self.hp} max_hp: {self.max_hp} ATK {self.attack} DEF {self.defence} known:\n"
        for attack in self.known_attacks:
            out += f"   {attack}\n"
        return out
    
def load_pokemon(file_name:str):
    with open(file_name, "r") as file:
        data = yaml.load(file, Loader)

    attack_data:dict = data["attacks"]
    pokemon_data:dict = data["pokemon"]
    
    attacks:dict[str, Attack] = {}
    for name in attack_data:
        data = attack_data[name]
        attack = Attack(name, PokemonType[data["type"]], data["power"])
        attacks[name] = attack
        
    pokemon:list[Pokemon] = []
    for name in pokemon_data:
        data = pokemon_data[name]
        known = []
        for attack_name in data["known_attacks"]:
            if attack_name not in attacks: 
                raise ValueError(f"Pokemon {name} has attack {attack_name} which is unknown in the system")
            known.append(attacks[attack_name])
        pokemon.append(Pokemon(
            name=name,
            type=PokemonType[data["type"]],
            level=data["level"],
            attack=data["attack"],
            defence=data["defence"],
            hp=data["hp"],
            attacks=known
        ))
        
    
    return pokemon