from enum import Enum
from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        instance = args[0] if args else None
        method_name = f"{instance.__class__.__name__}.{func.__name__}" if instance else func.__name__

        if instance and isinstance(instance, Vector2d):
            arguments = instance.x, instance.y
        else:
            arguments = args[1:]

        print(f"Nazwa kwalifikowana: {method_name}")
        print(f"Argumenty: {arguments}")
        result = func(*args, **kwargs)
        return result

    return wrapper

def log_to(file):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            instance = args[0] if args else None
            method_name = f"{instance.__class__.__name__}.{func.__name__}" if instance else func.__name__
            arguments = args[1:]
            log_entry = f"{method_name} | {arguments}\n"
            with open(f"{file}.txt", "a") as log_file:
                log_file.write(log_entry)
            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


class Vector2d:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

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
    
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

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
            