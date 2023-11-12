from typing import List
from model.core import MoveDirection, Vector2d
from model.animal import Animal
from model.map import RectangularMap

class Simulation:
    def __init__(self, directions: List[MoveDirection], positions: List[Vector2d]):
        self.directions = directions
        self.animals = [Animal(position) for position in positions]
<<<<<<< HEAD
        self.map = RectangularMap(4, 4)
=======
        self.map = RectangularMap(self.width, self.height)
>>>>>>> fd33359ed8c65d0f0bd478e05dcc7795f1559969

    def run(self):
        num_animals = len(self.animals)
        current_animal_index = 0

        for direction in self.directions:
            current_animal = self.animals[current_animal_index]
            current_animal.move(direction, self.map)
            print(f"Zwierzę {current_animal_index}: {current_animal}")

            # Przełącz do następnego zwierzęcia w cyklu
            current_animal_index = (current_animal_index + 1) % num_animals


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
                print(f"Ignoring unknown direction: {arg}")
        return directions
