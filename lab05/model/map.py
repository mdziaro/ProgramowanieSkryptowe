from model.core import Vector2d, MoveDirection
from model.interface import IMoveValidator, IWorldMap
from model.animal import Animal
from view import MapVisualizer
from exceptions import PositionAlreadyOccupiedError

class WorldMap(IMoveValidator, IWorldMap):
    def __init__(self):
        self.animals = {}

    def isPositionOccupied(self, position: Vector2d) -> bool:
        return position in self.animals

    def place(self, animal) -> any:
        if not self.isPositionOccupied(animal.position) and self.isInsideMap(animal.position):
            self.animals[animal.position] = animal
            return True
        else:
            raise PositionAlreadyOccupiedError(animal.position)

    def removeAnimal(self, animal) -> None:
        if animal.position in self.animals:
            del self.animals[animal.position]

    def canMoveTo(self, position: Vector2d) -> bool:
        return self.isInsideMap(position) and not self.isPositionOccupied(position)

    def isOccupied(self, position: Vector2d) -> bool:
        return self.isPositionOccupied(position)

    def objectAt(self, position: Vector2d):
        return self.animals.get(position, None)
    
    def move(self, animal: Animal, direction: MoveDirection) -> None:
        new_position = animal.position

        if direction == MoveDirection.FORWARD:
            new_position += animal.orientation.toUnitVector()
        elif direction == MoveDirection.BACKWARD:
            new_position -= animal.orientation.toUnitVector()
        if direction == MoveDirection.RIGHT:
            new_position += animal.orientation.toUnitVector()
        elif direction == MoveDirection.LEFT:
            new_position -= animal.orientation.toUnitVector()

        if self.canMoveTo(new_position):
            self.removeAnimal(animal)
            animal.move(direction, self)
            self.place(animal)
    
    
class RectangularMap(WorldMap):
    def __init__(self, width: int, height: int):
        super().__init__()
        self.width = width
        self.height = height
        self.upperRight = Vector2d(self.width, self.height)
        self.lowerLeft = Vector2d(0, 0)

    def isInsideMap(self, position: Vector2d) -> bool:
        return 0 <= position.get_x() <= self.width and 0 <= position.get_y() <= self.height

    
    def __str__(self) -> str:
        visualizer = MapVisualizer(self)
        return visualizer.draw(self.lowerLeft, self.upperRight)

class InfiniteMap(WorldMap):
    def __init__(self):
        super().__init__()
        self.animals = {}

    def isPositionOccupied(self, position: Vector2d) -> bool:
        return position in self.animals

    def place(self, animal) -> bool:
        if not self.isPositionOccupied(animal.position):
            self.animals[animal.position] = animal
            return True
        return False

    def removeAnimal(self, animal) -> None:
        if animal.position in self.animals:
            del self.animals[animal.position]

    def canMoveTo(self, position: Vector2d) -> bool:
        return not self.isPositionOccupied(position)

    def isInsideMap(self, position: Vector2d) -> bool:
        return True  # Infinite map, always inside

    def __str__(self) -> str:
        if not self.animals:
            return "Empty map"

        min_x = min(animal.position.x for animal in self.animals.values())
        max_x = max(animal.position.x for animal in self.animals.values())
        min_y = min(animal.position.y for animal in self.animals.values())
        max_y = max(animal.position.y for animal in self.animals.values())

        visualizer = MapVisualizer(self)
        return visualizer.draw(Vector2d(min_x, min_y), Vector2d(max_x, max_y))