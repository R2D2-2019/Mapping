from algorithm import Algorithms
class mapping:
    def __init__(self):
        self.current_location = [10, 10]#*2
        self.new_location = [10.0001,10.0001]
        self.coordinates_movement = [0,0]
        self.robot_movement_x = 0
        self.robot_movement_y = 0
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
                            200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,
                            200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200]

    ## Documentation for place_obstacle_on_map
    #  This function makes an object seen by the sensor, as a coordinate that can be placed on the 2d grid.
    #  which_degree is the degree from the object that is detected. Calculated from way of facing to the object (0-360) 
    def place_obstacle_on_map(self, which_degree):
        assert type(which_degree) is int, "which_degree invalid type"
        lidar_distance = self.lidar_data[which_degree]
        distances = Algorithms().from_lidar_to_coordinate(which_degree, lidar_distance)
        return distances
    
    ## Documentation for update_robot_location
    #  This function updates to robots location compared to what it was before,
    #  this way it expands the map if it senses new obstacles on a new location.
    #  coordinate is needed to place a seen obstacle on the right spot on the 2d grid.
    def update_robot_location(self, coordinate):
        self.robot_movement_x += Algorithms().measure_distance(self.current_location[0], self.current_location[1], self.current_location[0], self.new_location[0]) # meters
        self.robot_movement_y += Algorithms().measure_distance(self.current_location[0], self.current_location[1], self.new_location[1], self.current_location[1])
        if self.current_location[0] < self.new_location[0] and self.current_location[1] < self.new_location[1]: # xy+
            coordinate[0] += round(self.robot_movement_x)
            coordinate[1] += round(self.robot_movement_y)
        elif self.current_location[0] < self.new_location[0]: # x+
            coordinate[0] += round(self.robot_movement_x)
        elif self.current_location[1] < self.new_location[1]: # y+
            coordinate[1] += round(self.robot_movement_y)
        elif self.current_location[0] > self.new_location[0] and self.current_location[1] > self.new_location[1]: # xy-
            coordinate[0] -= round(self.robot_movement_x)
            coordinate[1] -= round(self.robot_movement_y)
        elif self.current_location[0] > self.new_location[0]: # x-
            coordinate[0] -= round(self.robot_movement_x)
        elif self.current_location[1] > self.new_location[1]: # y- 
            coordinate[1] -= round(self.robot_movement_y)
        self.current_location = self.new_location

