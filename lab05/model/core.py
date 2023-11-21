from enum import Enum
from functools import wraps


class Vector2d:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    
    def __add__(self, other: 'Vector2d') -> 'Vector2d':
        return Vector2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector2d') -> 'Vector2d':
        return Vector2d(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        if isinstance(other, Vector2d):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.x, self.y))
    
    def log(fn):
        def log_helper(*args, **kwargs):
            print("Nazwa kwalifikowana: Vector2d.{}".format(fn.__name__))
            print("Argumenty: {}".format(" ".join([arg.__str__() for arg in args])))
            return fn(*args, **kwargs)

        return log_helper
    
    def log_to(file: "str"):
        def log_decorator(fn):
            def log_helper(*args, **kwargs):
                with open(file+".txt", "a+") as f:
                    f.write("Vector2d.{} | {}\n".format(fn.__name__, " ".join([arg.__str__() for arg in args])))
                return fn(*args, **kwargs)
            return log_helper
        return log_decorator

    def get_x(self) -> int:
        return self._x
    
    def get_y(self) -> int:
        return self._y
    
    @property
    @log_to(file=".logs")
    def x(self) -> int:
        return self.get_x() 

    @property
    def y(self) -> int:
        return self.get_y()
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __repr__(self) -> str:
        return "({},{})".format(self._x, self._y)
    
    @log_to(file=".logs")
    def add(self, other_Vector2d: 'Vector2d') -> 'Vector2d':
        return Vector2d(self._x + other_Vector2d.get_x(), self._y + other_Vector2d.get_y())
    
    def subtract(self, other_Vector2d: 'Vector2d') -> 'Vector2d':
        return Vector2d(self._x - other_Vector2d.get_x(), self._y - other_Vector2d.get_y())

class MoveDirection(Enum):
    FORWARD = "f"
    BACKWARD = "b"
    RIGHT = "r"
    LEFT = "l"

    def toUnitVector(self) -> Vector2d:
        if self == MoveDirection.FORWARD:
            return Vector2d(0, 1)
        elif self == MoveDirection.BACKWARD:
            return Vector2d(0, -1)
        elif self == MoveDirection.RIGHT:
            return Vector2d(1, 0)
        elif self == MoveDirection.LEFT:
            return Vector2d(-1, 0)

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
            