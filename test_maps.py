from mapping_interface import PointState
from key_value_map import keyValueMap
from list_map import ListMap
from quadtree_map import quadtreeMap
from quadtree_map import rectangle
from cartesian_coordinate import CartesianCoordinate
from memory_profiler import profile
from time import time
from random import randrange
from random import sample
from extract_test_data import extract_data


name = "map_test.log"
fp = open(name, "w+")


@profile(stream=fp, precision=4)
def test_add_to_map(t_map, point):
    t_map.add_point_cartesian(point, PointState.occupied)


maps = [keyValueMap(), ListMap()]

root_size = rectangle(0, 0, 50, 50)
maps.append(quadtreeMap(root_size, 4))
points = []

for i in range(1000):                                           # Generate random points
    points.append(CartesianCoordinate(randrange(0, 100, 1), randrange(0, 100, 1)))

start = time()
for p in points:
    test_add_to_map(maps[0], p)
end = time()

fp.writelines("<===KEY_VALUE\r\n")                              # Map identification
fp.writelines(str(float(end-start)) + "\r\n")                   # Write the time to the file

start = time()
for p in points:
    test_add_to_map(maps[1], p)
end = time()

fp.writelines("<===LIST_MAP\r\n")                               # Map identification
fp.writelines(str(float(end-start)) + "\r\n")                   # Write the time to the file

test_map = maps[2]
start = time()
for p in points:
    test_add_to_map(maps[2], p)
end = time()

fp.writelines("<===QUAD_TREE_MAP\r\n")                          # Map identification
fp.writelines(str(float(end-start)) + "\r\n")                   # Write the time to the file
fp.close()

extract_data("map_test.log")                                    # Extract the data from the file

for m in maps:
    print(len(m.get_map_points()), "\t", list(m.get_map_points()))

for m in maps:
    print(m, "\n\n")
