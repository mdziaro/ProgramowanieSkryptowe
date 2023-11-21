import pytest
from model.core import MapDirection, Vector2d, MoveDirection
from model.animal import Animal
from model.map import RectangularMap, RectangularMap
from functools import partial

@pytest.fixture
def animal():
    yield Animal(Vector2d(2, 2))

@pytest.fixture
def validator():
    yield RectangularMap(4,4)


def test_Animal_isAt(animal: Animal):
    assert animal.isAt(Vector2d(2, 2))

def test_Animal_print(animal: Animal):
    assert str(animal) == "↑"

def test_Animal_move_north(animal: Animal, validator: RectangularMap):
    assert animal.orientation == MapDirection.NORTH
    animal.move(MoveDirection.FORWARD, validator)
    animal.move(MoveDirection.FORWARD, validator)
    assert animal.isAt(Vector2d(2, 4))
    animal.move(MoveDirection.FORWARD, validator)
    animal.move(MoveDirection.FORWARD, validator)
    assert animal.isAt(Vector2d(2, 4))
    animal.move(MoveDirection.BACKWARD, validator)
    assert animal.isAt(Vector2d(2, 3))

def test_Animal_move_south(animal: Animal, validator: RectangularMap):
    assert animal.orientation == MapDirection.NORTH
    animal.move(MoveDirection.BACKWARD, validator)
    animal.move(MoveDirection.BACKWARD, validator)
    assert animal.isAt(Vector2d(2, 0))
    animal.move(MoveDirection.BACKWARD, validator)
    animal.move(MoveDirection.BACKWARD, validator)
    assert animal.isAt(Vector2d(2, 0))
    animal.move(MoveDirection.FORWARD, validator)
    assert animal.isAt(Vector2d(2, 1))

def test_Animal_move_east(animal: Animal, validator: RectangularMap):
    animal.move(MoveDirection.RIGHT, validator)
    assert animal.orientation == MapDirection.EAST
    animal.move(MoveDirection.FORWARD, validator)
    animal.move(MoveDirection.FORWARD, validator)
    assert animal.isAt(Vector2d(4, 2))
    animal.move(MoveDirection.FORWARD, validator)
    animal.move(MoveDirection.FORWARD, validator)
    assert animal.isAt(Vector2d(4, 2))
    animal.move(MoveDirection.BACKWARD, validator)
    assert animal.isAt(Vector2d(3, 2))

def test_Animal_move_west(animal: Animal, validator: RectangularMap):
    animal.move(MoveDirection.LEFT, validator)
    assert animal.orientation == MapDirection.WEST
    animal.move(MoveDirection.FORWARD, validator)
    animal.move(MoveDirection.FORWARD, validator)
    assert animal.isAt(Vector2d(0, 2))
    animal.move(MoveDirection.FORWARD, validator)
    animal.move(MoveDirection.FORWARD, validator)
    assert animal.isAt(Vector2d(0, 2))
    animal.move(MoveDirection.BACKWARD, validator)
    assert animal.isAt(Vector2d(1, 2))
