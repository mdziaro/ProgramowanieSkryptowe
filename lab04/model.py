from enum import Enum
from typing import Self

class MapDirection(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def __str__(self) -> str:
        if self == MapDirection.EAST:
            return "→"
        elif self == MapDirection.WEST:
            return "←"
        elif self == MapDirection.SOUTH:
            return "↓"
        elif self == MapDirection.NORTH:
            return "↑"
        else:
            return str(self)

    def next(self) -> "MapDirection":
        return MapDirection((self.value + 1) % 4)

    def previous(self) -> "MapDirection":
        return MapDirection((self.value - 1) % 4)

    def toUnitVector(self) -> "Vector2d":
        if self == MapDirection.NORTH:
            return Vector2d(0, 1)
        elif self == MapDirection.EAST:
            return Vector2d(1, 0)
        elif self == MapDirection.SOUTH:
            return Vector2d(0, -1)
        elif self == MapDirection.WEST:
            return Vector2d(-1, 0)

class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y