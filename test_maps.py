from mapping_interface import PointState
from key_value_map import keyValueMap
from list_map import ListMap
from quadtree_map import quadtreeMap
from quadtree_map import rectangle
from cartesian_coordinate import CartesianCoordinate

maps = []
maps.append(keyValueMap())
maps.append(ListMap())

root_size = rectangle(0, 0, 50, 50)
maps.append(quadtreeMap(root_size, 4))
points = []
points.append(CartesianCoordinate(-11, -11))
points.append(CartesianCoordinate(0, 0))
points.append(CartesianCoordinate(11, 11))
points.append(CartesianCoordinate(-1, 1))
points.append(CartesianCoordinate(1, -1))

for map in maps:
    for point in points:
        map.add_point_cartesian(point, PointState.occupied)

    print(map.get_map_points())
    print(map)
