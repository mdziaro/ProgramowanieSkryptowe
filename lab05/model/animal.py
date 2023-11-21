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

    def move(self, direction: MoveDirection, validator: IMoveValidator, move_logic_func=None) -> None:
        if move_logic_func is None:
            move_logic_func = self.default_move_logic

        move_logic_func(self, direction, validator)

    def default_move_logic(self, animal, direction, validator) -> None:
        if direction == MoveDirection.RIGHT:
            animal.orientation = animal.orientation.next()
        elif direction == MoveDirection.LEFT:
            animal.orientation = animal.orientation.previous()
        elif direction == MoveDirection.FORWARD:
            new_position = animal.position + animal.orientation.toUnitVector()
            animal.try_move(new_position, validator)
        elif direction == MoveDirection.BACKWARD:
            new_position = animal.position - animal.orientation.toUnitVector()
            animal.try_move(new_position, validator)

    def try_move(self, new_position: Vector2d, validator: IMoveValidator) -> None:
        if validator.canMoveTo(new_position):
            self.position = new_position

    def __repr__(self) -> str:
        return str(self.orientation)