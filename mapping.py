from algorithm import Algorithms
class mapping:
    """
    Base class for mapping
    Works with outer modules
    Processes outer frame data to make the map
    """
    
    def __init__(self):
        """
        Setup the fake values from other sensors
        Initializes the movement from the robot
        """

        self.current_location = [10, 10]#*2
        """ The current location from the robot in world coordinates """

        self.new_location = [10.0001,10.0001]
        """ The new incomming location from the CAN-bus in world coordinates """

        self.coordinates_movement = [0,0]
        """ Coordinate from the robot based on 2d grid map """

        self.robot_movement_x = 0
        """ X direction on the 2d grid """

        self.robot_movement_y = 0
        """ Y direction on the 2d grid """

        self.lidar_data =   [200,200,200,200,200,200,200,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,200,200,200,200,
                            200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,
                            200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,
                            200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,
                            200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,
                            200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,
                            200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,
                            200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,
                            200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,
                            200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,
                            200,200,200,20,20,20,20,20,20,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,
                            200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200]
        """ Data from the lidar, a list of 360 integers, every integer is a distance """
 
    def place_obstacle_on_map(self, which_degree):
        """
        Documentation for place_obstacle_on_map
        This function makes an object seen by the sensor, as a coordinate that can be placed on the 2d grid.
        which_degree is the degree from the object that is detected. Calculated from way of facing to the object (0-360)
        """
        assert type(which_degree) is int, "which_degree invalid type"
        lidar_distance = self.lidar_data[which_degree]
        distances = Algorithms().from_lidar_to_coordinate(which_degree, lidar_distance)
        return distances
    

    def update_robot_location(self, coordinate):
        """
        Documentation for update_robot_location
        This function updates to robots location compared to what it was before,
        this way it expands the map if it senses new obstacles on a new location.
        coordinate is needed to place a seen obstacle on the right spot on the 2d grid.        
        """
        self.robot_movement_x += Algorithms().measure_distance(self.current_location[0], self.current_location[1],
                                                               self.current_location[0], self.new_location[0]) # meters
        self.robot_movement_y += Algorithms().measure_distance(self.current_location[0], self.current_location[1],
                                                               self.new_location[1], self.current_location[1])
        if (self.current_location[0] < self.new_location[0] and
            self.current_location[1] < self.new_location[1]): # xy+
            coordinate[0] += round(self.robot_movement_x)
            coordinate[1] += round(self.robot_movement_y)
        elif self.current_location[0] < self.new_location[0]: # x+
            coordinate[0] += round(self.robot_movement_x)
        elif self.current_location[1] < self.new_location[1]: # y+
            coordinate[1] += round(self.robot_movement_y)
        elif (self.current_location[0] > self.new_location[0] and 
              self.current_location[1] > self.new_location[1]): # xy-
            coordinate[0] -= round(self.robot_movement_x)
            coordinate[1] -= round(self.robot_movement_y)
        elif self.current_location[0] > self.new_location[0]: # x-
            coordinate[0] -= round(self.robot_movement_x)
        elif self.current_location[1] > self.new_location[1]: # y- 
            coordinate[1] -= round(self.robot_movement_y)
        self.current_location = self.new_location

