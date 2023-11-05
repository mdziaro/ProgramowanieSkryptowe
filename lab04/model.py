from enum import Enum
from typing import Tuple

class Vector2d:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other: 'Vector2d') -> 'Vector2d':
        return Vector2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector2d') -> 'Vector2d':
        return Vector2d(self.x - other.x, self.y - other.y)

    def __eq__(self, other: 'Vector2d') -> bool:
        return self.x == other.x and self.y == other.y

class MoveDirection(Enum):
    FORWARD = "f"
    BACKWARD = "b"
    RIGHT = "r"
    LEFT = "l"

class MapDirection(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def __str__(self) -> str:
        directions = ["↑", "→", "↓", "←"]
        return directions[self.value]

    def next(self) -> 'MapDirection':
        return MapDirection((self.value + 1) % 4)

    def previous(self) -> 'MapDirection':
        return MapDirection((self.value - 1) % 4)

    def toUnitVector(self) -> Vector2d:
        if self == MapDirection.NORTH:
            return Vector2d(0, 1)
        elif self == MapDirection.EAST:
            return Vector2d(1, 0)
        elif self == MapDirection.SOUTH:
            return Vector2d(0, -1)
        elif self == MapDirection.WEST:
            return Vector2d(-1, 0)

class Animal:
    def __init__(self, position: Vector2d, orientation: MapDirection = MapDirection.NORTH):
        self.position = position
        self.orientation = orientation

    def __str__(self) -> str:
        return f"({self.position.x},{self.position.y}) {self.orientation}"

    def isAt(self, position: Vector2d) -> bool:
        return self.position == position

    def move(self, direction: MoveDirection) -> None:
        if direction == MoveDirection.RIGHT:
            self.orientation = self.orientation.next()
        elif direction == MoveDirection.LEFT:
            self.orientation = self.orientation.previous()
        elif direction == MoveDirection.FORWARD:
            new_position = self.position + self.orientation.toUnitVector()
            if self.isInsideMap(new_position):
                self.position = new_position
        elif direction == MoveDirection.BACKWARD:
            new_position = self.position - self.orientation.toUnitVector()
            if self.isInsideMap(new_position):
                self.position = new_position

    def isInsideMap(self, position: Vector2d) -> bool:
        return 0 <= position.x <= 4 and 0 <= position.y <= 4
