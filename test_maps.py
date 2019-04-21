from key_value_map import keyValueMap
from mapping_interface import PointState
from list_map import ListMap
from cartesian_coordinate import CartesianCoordinate

maps = []
maps.append(keyValueMap())
maps.append(ListMap())
points = []
points.append(CartesianCoordinate(-11, -11))
points.append(CartesianCoordinate(0, 0))
points.append(CartesianCoordinate(11, 11))
points.append(CartesianCoordinate(-1, 1))
points.append(CartesianCoordinate(1, -1))

for map in maps:
    for point in points:
        map.add_point_cartesian(point, PointState.occupied)

    print(map)
    print(map.get_bot_right_point())
    print(map.get_top_left_point())
