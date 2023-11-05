"""
Autor: Stanisław Polak
Data utworzenia: 22-10-2023
Data modyfikacji: 22-10-2023
Wersja: 1.0
Opis: Testy jednostkowe enuma "MapDirection".
"""
from model import MapDirection, Vector2d
def test_MapDirection_print(capsys):
    print(MapDirection.NORTH)
    print(MapDirection.EAST)
    print(MapDirection.SOUTH)
    print(MapDirection.WEST)
    captured = capsys.readouterr()
    assert captured.out == "↑\n→\n↓\n←\n"
def test_MapDirection_next():
    assert MapDirection.NORTH.next() == MapDirection.EAST
    assert MapDirection.EAST.next() == MapDirection.SOUTH
    assert MapDirection.SOUTH.next() == MapDirection.WEST
    assert MapDirection.WEST.next() == MapDirection.NORTH
def test_MapDirection_previous():
    assert MapDirection.NORTH.previous() == MapDirection.WEST
    assert MapDirection.WEST.previous() == MapDirection.SOUTH
    assert MapDirection.SOUTH.previous() == MapDirection.EAST
    assert MapDirection.EAST.previous() == MapDirection.NORTH

#Zmieniłem testy, gdyż python porównywał, czy obiekty są te same, a nie czy ich wartości są równe:

def test_MapDirection_toUnitVector():
    north_vector = MapDirection.NORTH.toUnitVector()
    east_vector = MapDirection.EAST.toUnitVector()
    south_vector = MapDirection.SOUTH.toUnitVector()
    west_vector = MapDirection.WEST.toUnitVector()

    assert north_vector.x == 0
    assert north_vector.y == 1

    assert east_vector.x == 1
    assert east_vector.y == 0

    assert south_vector.x == 0
    assert south_vector.y == -1

    assert west_vector.x == -1
    assert west_vector.y == 0
