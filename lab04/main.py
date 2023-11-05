import sys
from model import MoveDirection, Vector2d
from controller import Simulation, OptionsParser

directions: list[MoveDirection] = OptionsParser.parse(sys.argv[1:]) 
positions: list[Vector2d] = [Vector2d(2,2), Vector2d(3,4)] # Pozycje początkowe dla zwierząt, odpowiednio, (2,2) oraz (3,4) 
simulation: Simulation = Simulation(directions, positions)
simulation.run()     

#python3 main.py f b r l f f r r f f f f f f f f
"""
Zwierzę 0 : (2,3) ↑
Zwierzę 1 : (3,3) ↑
Zwierzę 0 : (2,3) →
Zwierzę 1 : (3,3) ←
Zwierzę 0 : (3,3) →
Zwierzę 1 : (2,3) ←
Zwierzę 0 : (3,3) ↓
Zwierzę 1 : (2,3) ↑
Zwierzę 0 : (3,2) ↓
Zwierzę 1 : (2,4) ↑
Zwierzę 0 : (3,1) ↓
Zwierzę 1 : (2,4) ↑
Zwierzę 0 : (3,0) ↓
Zwierzę 1 : (2,4) ↑
Zwierzę 0 : (3,0) ↓
Zwierzę 1 : (2,4) ↑
"""