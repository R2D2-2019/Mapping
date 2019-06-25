
from mapping_interface import PointState
from key_value_map import KeyValueMap
from list_map import ListMap
from quadtree_map import QuadtreeMap
from quadtree_map import Rectangle
from cartesian_coordinate import CartesianCoordinate

maps = []
maps.append(KeyValueMap())
maps.append(ListMap())

root_size = Rectangle(0, 0, 0, 0)
maps.append(QuadtreeMap(root_size, 4))
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