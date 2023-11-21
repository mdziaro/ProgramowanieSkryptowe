from model.core import MapDirection, MoveDirection, Vector2d
from model.interface import IMoveValidator

class Animal:
    def __init__(self, position: Vector2d, orientation: MapDirection = MapDirection.NORTH):
        self.position = position
        self.orientation = orientation

    def __str__(self) -> str:
        return str(self.orientation)

    def isAt(self, position: Vector2d) -> bool:
        return self.position == position

    def move(self, direction: MoveDirection, validator: IMoveValidator) -> None:
        if direction == MoveDirection.RIGHT:
            self.orientation = self.orientation.next()
        elif direction == MoveDirection.LEFT:
            self.orientation = self.orientation.previous()
        elif direction == MoveDirection.FORWARD:
            new_position = self.position + self.orientation.toUnitVector()
            if validator.canMoveTo(new_position):
                self.position = new_position
        elif direction == MoveDirection.BACKWARD:
            new_position = self.position - self.orientation.toUnitVector()
            if validator.canMoveTo(new_position):
                self.position = new_position

    def __repr__(self) -> str:
        return str(self.orientation)