from enum import Enum
import random

class Weather(Enum):
    NORMAL = 0
    SUNNY = 1
    RAINING = 2
    
weather_chance = [9, 1, 1]
weather_change_chance = 0.1
    
class Terrain(Enum):
    NORMAL = 0
    GRASSY = 1
    ELECTRIC = 2
    
terrain_chance = [9, 1, 1]
    
def pick_random_weather() -> Weather:
    return random.choices([*Weather], weather_chance)[0]

def pick_different_weather(current_weather:Weather) -> Weather:
    all_weather = [*Weather]
    all_weather.remove(current_weather)
    return random.choice(all_weather)

def pick_random_terrain() -> Terrain:
    return random.choices([*Terrain], terrain_chance)[0]
    
class Field:
    def __init__(self, terrain:Terrain, weather:Weather) -> None:
        self.terrain = terrain
        self.weather = weather
        
    def update(self):
        """updates the changes to field conditions"""
        new_weather = pick_different_weather(self.weather)
        # TODO: print weather changes in game
        self.weather = new_weather

        
    @staticmethod
    def create() -> Field:
        return Field(
            pick_random_terrain(), 
            pick_random_weather()
        )