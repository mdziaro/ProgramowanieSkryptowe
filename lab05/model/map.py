from model.core import Vector2d, MoveDirection
from model.animal import Animal
from model.interface import IMoveValidator, IWorldMap
from view import MapVisualizer

class RectangularMap(IMoveValidator, IWorldMap):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.animals: dict[Vector2d, Animal] = {}

    def isInsideMap(self, position: Vector2d) -> bool:
        return 0 <= position.x < self.width and 0 <= position.y < self.height

    def isPositionOccupied(self, position: Vector2d) -> bool:
        return position in self.animals

    def place(self, animal: Animal) -> bool:
        if not self.isPositionOccupied(animal.position) and self.isInsideMap(animal.position):
            self.animals[animal.position] = animal
            return True
        return False

    def removeAnimal(self, animal: Animal) -> None:
        if animal.position in self.animals:
            del self.animals[animal.position]

    def move(self, animal: Animal, direction: MoveDirection) -> None:
        new_position = animal.position

        if direction == MoveDirection.FORWARD:
            new_position += animal.orientation.toUnitVector()
        elif direction == MoveDirection.BACKWARD:
            new_position -= animal.orientation.toUnitVector()

        if self.canMoveTo(new_position):
            self.removeAnimal(animal)
            animal.move(direction, self)
            self.place(animal)

    def canMoveTo(self, position: Vector2d) -> bool:
        return self.isInsideMap(position) and not self.isPositionOccupied(position)

    def isOccupied(self, position: Vector2d) -> bool:
        return self.isPositionOccupied(position)

    def objectAt(self, position: Vector2d) -> Animal | None:
        return self.animals.get(position, None)

    def __str__(self) -> str:
        visualizer = MapVisualizer(self)
        return visualizer.draw()
