#!/usr/bin/env python3
import sys
from model.core import Vector2d, MoveDirection
from model.interface import IWorldMap
from model.map import RectangularMap as MyRectangularMap
from model.map import InfiniteMap as MyInfiniteMap
from controller import Simulation, OptionsParser


directions: list[MoveDirection] = OptionsParser.parse(sys.argv[1:])
positions: list[Vector2d] = [Vector2d(2, 2), Vector2d(3, 4), Vector2d(0, 4)]

# Poprzednio
# simulation: Simulation = Simulation(directions, positions)
# simulation.run()

# Obecnie
map: IWorldMap = MyRectangularMap(10, 10)
#map: IWorldMap = MyInfiniteMap()

simulation: Simulation = Simulation(directions, positions, map)
simulation.run()

# Testowanie dekoratorów
v1 = Vector2d(2, 2)
v2 = v1.add(Vector2d(1, 1))
print(v2)  # Wyświetli się informacja z dekoratora @log
print(v2.x)  # Wyświetli się informacja z dekoratora @log