"""
Autor: Stanisław Polak
Data utworzenia: 22-10-2023
Data modyfikacji: 22-10-2023
Wersja: 1.0
Opis: Testy jednostkowe klasy "Simulation".
"""
#Zmodyfikowałem testy, by porównywały wartości obiektów, a nie obiekty
import pytest
from model.core import Vector2d, MoveDirection, MapDirection
from controller import Simulation, OptionsParser
from model.map import RectangularMap
from functools import partial

@pytest.fixture
def rectangular_map():
    return RectangularMap(10, 10)

# Updated fixture to use rectangular_map fixture
@pytest.fixture
def simulation_for_two_animals(rectangular_map):
    args = "f b r l f f r r f f f f f f f f".split(" ")
    directions: list[MoveDirection] = OptionsParser.parse(args)
    positions: list[Vector2d] = [Vector2d(2, 2), Vector2d(3, 4)]
    yield Simulation(directions, positions, rectangular_map)

# Updated fixture to use rectangular_map fixture
@pytest.fixture
def simulation_for_three_animals(rectangular_map):
    args = "f b r l f f r r f f f f f f f f".split(" ")
    directions: list[MoveDirection] = OptionsParser.parse(args)
    positions: list[Vector2d] = [Vector2d(2, 2), Vector2d(3, 4), Vector2d(0, 4)]
    yield Simulation(directions, positions, rectangular_map)

def test_Simulation_run_for_two_animals(simulation_for_two_animals: Simulation):
    simulation_for_two_animals.run()
    assert simulation_for_two_animals.animals[0].position.x == 2
    assert simulation_for_two_animals.animals[0].position.y == 3
    assert simulation_for_two_animals.animals[0].orientation == MapDirection.EAST
    assert simulation_for_two_animals.animals[1].position.x == 3
    assert simulation_for_two_animals.animals[1].position.y == 3
    assert simulation_for_two_animals.animals[1].orientation == MapDirection.WEST

def test_Simulation_run_for_three_animals(simulation_for_three_animals: Simulation):
    simulation_for_three_animals.run()
    assert simulation_for_three_animals.animals[0].position.x == 2
    assert simulation_for_three_animals.animals[0].position.y == 5
    assert simulation_for_three_animals.animals[0].orientation == MapDirection.NORTH
    assert simulation_for_three_animals.animals[1].position.x == 5
    assert simulation_for_three_animals.animals[1].position.y == 4
    assert simulation_for_three_animals.animals[1].orientation == MapDirection.EAST
    assert simulation_for_three_animals.animals[2].position.x == 4
    assert simulation_for_three_animals.animals[2].position.y == 4
    assert simulation_for_three_animals.animals[2].orientation == MapDirection.EAST