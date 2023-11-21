from typing import List
from time import sleep
from model.interface import IWorldMap
from model.core import MoveDirection, Vector2d
from model.animal import Animal

class Simulation:
    def __init__(self, directions: List[MoveDirection], positions: List[Vector2d], world_map: IWorldMap):
        self.directions = directions
        self.map = world_map
        self.animals = []
        for position in positions:
            if self.map.place(Animal(position)):
                self.animals.append(Animal(position))

    def run(self):
        num_animals = len(self.animals)
        current_animal_index = 0

        for direction in self.directions:
            # Wypisanie aktualnego stanu mapy
            print(self.map)

            current_animal = self.animals[current_animal_index]
            self.map.move(current_animal, direction)
            print(f"Zwierzę {current_animal_index}: {current_animal}")
            

            # Przełącz do następnego zwierzęcia w cyklu
            current_animal_index = (current_animal_index + 1) % num_animals

            # Uśpienie procesu na jedną sekundę
            sleep(1)



class OptionsParser:
    @staticmethod
    def parse(args: List[str]) -> List[MoveDirection]:
        directions = []
        for arg in args:
            if arg == 'f':
                directions.append(MoveDirection.FORWARD)
            elif arg == 'b':
                directions.append(MoveDirection.BACKWARD)
            elif arg == 'r':
                directions.append(MoveDirection.RIGHT)
            elif arg == 'l':
                directions.append(MoveDirection.LEFT)
            else:
                raise ValueError(f'{arg} is not a legal move specification')
        return directions
