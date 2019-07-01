from mapping_interface import PointState
from key_value_map import KeyValueMap
from list_map import ListMap
from quadtree_map import QuadtreeMap
from quadtree_map import Rectangle
from cartesian_coordinate import CartesianCoordinate
from mapping import mapping

maps = []
maps.append(KeyValueMap())
maps.append(ListMap())

root_size = Rectangle(0, 0, 0, 0)
maps.append(QuadtreeMap(root_size, 2))
points = []

# function to generate the obstacle
def calcc():
    for degree in range(0, 360):
        if mapping().lidar_data[degree] < 50: #For now 5 in meters
            temp = mapping().place_obstacle_on_map(degree)
            print(temp)
            points.append(CartesianCoordinate(temp[0], temp[1]))

# function to give a fake update to expand the map with the same obstacle coordinate
def moved():
    for degree in range(0, 360):
        if mapping().lidar_data[degree] < 50: #For now 5 in meters
            temp1 = mapping().place_obstacle_on_map(degree)
            mapping().update_robot_location(temp1)
            print(temp1)
            points.append(CartesianCoordinate(temp1[0], temp1[1]))

calcc()

for map in maps:
    for point in points:
        map.add_point_cartesian(point, PointState.occupied)
    
    map.get_map_points()
    print(map)
moved()

for map in maps:
    for point in points:
        map.add_point_cartesian(point, PointState.occupied)
    
    map.get_map_points()
    print(map)