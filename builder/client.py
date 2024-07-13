from igloo_director import IglooDirector
from houseboat_director import HouseBoatDirector
from castle_director import CastleDirector

IGLOO = IglooDirector.construct()
HOUSEBOAT = HouseBoatDirector.construct()
CASTLE = CastleDirector.construct()

print(IGLOO.construction())
print(CASTLE.construction())
print(HOUSEBOAT.construction())
