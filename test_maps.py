from key_value_map import keyValueMap
from mapping_interface import PointState
from list_map import ListMap
from cartesian_coordinate import CartesianCoordinate

maps = []
maps.append(keyValueMap())
maps.append(ListMap())
points = []
points.append(CartesianCoordinate(-11,-11))
points.append(CartesianCoordinate(0,0))
points.append(CartesianCoordinate(11,11))

for map in maps:
	for point in points:
		map.addPointCartesian(point, PointState.occupied)

	print(map)
	print(map.getBotRightPoint())
	print(map.getTopLeftPoint())