"""
Autor: Stanisław Polak
Data utworzenia: 02-11-2023
Data modyfikacji: 02-11-2023
Wersja: 1.0
Opis: Testy integracyjne klas typu "IWorldMap".
"""
import pytest
from model.animal import Animal
from model.core import MoveDirection, Vector2d
from model.map import RectangularMap
from model.map import InfiniteMap
        
@pytest.fixture
def infinite_map():
    yield InfiniteMap()


@pytest.fixture
def rectangular_map_2_2():
    yield RectangularMap(2, 2)


@pytest.fixture
def rectangular_map_4_4():
    yield RectangularMap(4, 4)


@pytest.fixture
def animal1():
    yield Animal(Vector2d(0, 0))


@pytest.fixture
def animal2():
    yield Animal(Vector2d(3, 3))


@pytest.fixture
def animal3():
    yield Animal(Vector2d(1, 1))


@pytest.fixture
def animal4():
    yield Animal(Vector2d(-1, -2))


def test_for_map_2_2(
    rectangular_map_2_2: RectangularMap,
    animal1: Animal,
    animal2: Animal,
    animal3: Animal,
    animal4: Animal,
):
    # Test 'Animal' methods
    assert str(animal1) == "↑"
    assert repr(animal1) == "↑"
    assert animal1.isAt(Vector2d(0, 0)) is True
    animal1.move(MoveDirection.BACKWARD, rectangular_map_2_2)
    assert animal1.isAt(Vector2d(0, 0)) is True
    # Test 'IWorldMap' and 'IMoveValidator' methods
    assert rectangular_map_2_2.canMoveTo(Vector2d(-1, -1)) is False
    assert rectangular_map_2_2.canMoveTo(Vector2d(4, 4)) is False
    assert rectangular_map_2_2.canMoveTo(Vector2d(0, 0)) is True
    assert rectangular_map_2_2.place(animal1) is True
    assert rectangular_map_2_2.canMoveTo(Vector2d(0, 0)) is False
    assert rectangular_map_2_2.isOccupied(Vector2d(0, 0)) is True
    assert rectangular_map_2_2.place(animal1) is False
    assert rectangular_map_2_2.place(animal2) is False
    assert rectangular_map_2_2.place(animal3) is True
    assert rectangular_map_2_2.place(animal4) is False
    assert rectangular_map_2_2.objectAt(Vector2d(0, 0)) is animal1
    rectangular_map_2_2.move(animal1, MoveDirection.FORWARD)
    assert rectangular_map_2_2.objectAt(Vector2d(0, 0)) is None
    assert rectangular_map_2_2.objectAt(Vector2d(0, 1)) is animal1
    rectangular_map_2_2.move(animal1, MoveDirection.RIGHT)
    rectangular_map_2_2.move(animal1, MoveDirection.FORWARD)
    assert rectangular_map_2_2.objectAt(Vector2d(1, 1)) is not animal1
    assert rectangular_map_2_2.objectAt(Vector2d(1, 1)) is animal3
    rectangular_map_2_2.move(animal3, MoveDirection.FORWARD)
    rectangular_map_2_2.move(animal3, MoveDirection.FORWARD)
    rectangular_map_2_2.move(animal3, MoveDirection.FORWARD)
    assert rectangular_map_2_2.objectAt(Vector2d(1, 2)) is animal3


def test_for_map_4_4(
    rectangular_map_4_4: RectangularMap,
    animal1: Animal,
    animal2: Animal,
    animal3: Animal,
    animal4: Animal,
):
    assert rectangular_map_4_4.place(animal1) is True
    assert rectangular_map_4_4.place(animal1) is False
    assert rectangular_map_4_4.place(animal2) is True
    assert rectangular_map_4_4.place(animal3) is True
    assert rectangular_map_4_4.place(animal4) is False
    rectangular_map_4_4.move(animal3, MoveDirection.BACKWARD)
    assert rectangular_map_4_4.objectAt(Vector2d(0, 1)) is None
    assert rectangular_map_4_4.objectAt(Vector2d(1, 0)) is animal3
    rectangular_map_4_4.move(animal3, MoveDirection.LEFT)
    rectangular_map_4_4.move(animal3, MoveDirection.FORWARD)
    assert rectangular_map_4_4.objectAt(Vector2d(0, 0)) is animal1
    assert rectangular_map_4_4.objectAt(Vector2d(1, 1)) is animal3
    rectangular_map_4_4.move(animal2, MoveDirection.BACKWARD)
    rectangular_map_4_4.move(animal2, MoveDirection.BACKWARD)
    rectangular_map_4_4.move(animal2, MoveDirection.BACKWARD)
    assert rectangular_map_4_4.objectAt(Vector2d(3, 0)) is animal2
    rectangular_map_4_4.move(animal2, MoveDirection.BACKWARD)
    assert rectangular_map_4_4.objectAt(Vector2d(3, 0)) is animal2
    
def test_for_infinite_map(
    infinite_map: InfiniteMap,
    animal1: Animal,
    animal2: Animal,
    animal3: Animal,
    animal4: Animal,
):
    # Test 'Animal' methods
    assert animal1.isAt(Vector2d(0, 0)) is True
    animal1.move(MoveDirection.RIGHT, infinite_map)
    animal1.move(MoveDirection.FORWARD, infinite_map)
    assert animal1.isAt(Vector2d(1, 0)) is True
    animal1.move(MoveDirection.BACKWARD, infinite_map)
    animal1.move(MoveDirection.LEFT, infinite_map)
    assert animal1.isAt(Vector2d(0, 0)) is True
    animal1.move(MoveDirection.BACKWARD, infinite_map)
    assert animal1.isAt(Vector2d(0, -1)) is True
    animal1.move(MoveDirection.FORWARD, infinite_map)
    assert animal1.isAt(Vector2d(0, 0)) is True
    # Test 'IWorldMap' and 'IMoveValidator' methods
    assert infinite_map.canMoveTo(Vector2d(-1, -1)) is True
    assert infinite_map.canMoveTo(Vector2d(4, 4)) is True
    assert infinite_map.canMoveTo(Vector2d(0, 0)) is True
    assert infinite_map.place(animal1) is True
    assert infinite_map.canMoveTo(Vector2d(0, 0)) is False
    assert infinite_map.isOccupied(Vector2d(0, 0)) is True
    assert infinite_map.place(animal1) is False
    assert infinite_map.place(animal2) is True
    assert infinite_map.place(animal3) is True
    assert infinite_map.place(animal4) is True
    assert infinite_map.objectAt(Vector2d(0, 0)) is animal1
    infinite_map.move(animal1, MoveDirection.FORWARD)
    assert infinite_map.objectAt(Vector2d(0, 1)) is animal1
    assert infinite_map.objectAt(Vector2d(0, 0)) is None
    infinite_map.move(animal1, MoveDirection.RIGHT)
    infinite_map.move(animal1, MoveDirection.FORWARD)
    assert infinite_map.objectAt(Vector2d(1, 1)) is not animal1
    assert infinite_map.objectAt(Vector2d(1, 1)) is animal3
    infinite_map.move(animal4, MoveDirection.LEFT)
    infinite_map.move(animal4, MoveDirection.FORWARD)
    assert infinite_map.objectAt(Vector2d(-1, -2)) is None
    assert infinite_map.objectAt(Vector2d(-2, -2)) is animal4