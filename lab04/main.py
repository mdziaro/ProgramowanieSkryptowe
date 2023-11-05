from model import MapDirection, MoveDirection, Vector2d

print(MapDirection.EAST)                
print(MapDirection.EAST.next())         
print(MapDirection.EAST.previous())     
print(MapDirection.EAST.toUnitVector())
