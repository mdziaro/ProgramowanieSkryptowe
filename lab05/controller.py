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
        print(self.map)


class OptionsParser:
    @staticmethod
    def parse(args: List[str]) -> List[MoveDirection]:
        def map_to_direction(arg: str) -> MoveDirection:
            direction_mapping = {'f': MoveDirection.FORWARD, 'b': MoveDirection.BACKWARD, 'r': MoveDirection.RIGHT, 'l': MoveDirection.LEFT}
            if arg in direction_mapping:
                return direction_mapping[arg]
            else:
                raise ValueError(f'{arg} is not a legal move specification')

        return list(map(map_to_direction, args))
