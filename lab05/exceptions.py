from model.animal import Vector2d

class PositionAlreadyOccupiedError(Exception):
    def __init__(self, position: Vector2d):
        self.position = position
        super().__init__(f'Position {position} is already occupied')
