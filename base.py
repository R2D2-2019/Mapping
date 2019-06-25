
from mapping_interface import PointState
from key_value_map import KeyValueMap
from list_map import ListMap
from quadtree_map import QuadtreeMap
from quadtree_map import Rectangle
from cartesian_coordinate import CartesianCoordinate

class base_module_c:
    def __init__(self, base):
        """ 
        Construct a new base object for mapping.
        :param location: The location this module recieves from location detection.
        :param distance: The distance between the location and the obstacle.
        :param obstacle: The obstacle this module receives from ...
        :return: Returns nothing
        """
        self.NULL = 0
        self.x = 0
        self.y = 0
        self.location = []
        self.obstacles = [[]]
    
    def create_map(self):
        maps = []
        maps.append(KeyValueMap())
        maps.append(ListMap())

        root_size = Rectangle(0, 0, location.x, location.y)
        maps.append(QuadtreeMap(root_size, 4))
        points = []

        for obstacle in obstacle:
            points.append(CartesianCoordinate(obstacle.degree, obstacle.))


        for map in maps:
            for point in points:
                map.add_point_cartesian(point, PointState.occupied)

            print(map.get_map_points())
            print(map)
        
        
    
    def save_obstacle(self, obstacle, obstacles):
        obstacles= [[obstacle1],[obstacle2]]

    def get_obstacles(self):
        return self.obstacles


