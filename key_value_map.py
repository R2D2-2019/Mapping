from cartesian_coordinate import CartesianCoordinate
from mapping_interface import MapInterface
from mapping_interface import PointState


class KeyValueMap(MapInterface):
    """
    @brief Class keyValueMap provides functionality to create a map using keys and values.
    """

    def __init__(self):
        """
        @brief keyValueMap constructor used to create a basic key value map.
        """

        self.map = {}
        self.top_left_point = CartesianCoordinate(0, 0)
        self.bot_right_point = CartesianCoordinate(0, 0)

    def get_top_left_point(self):
        """
        @brief Method used to get the top_left_point of the key value map.
        @return A CartesianCoordinate containing the top left corner point of the key value map.
        """

        return self.top_left_point

    def get_bot_right_point(self):
        """
        @brief Method used to get the bot_right_point of the key value map.
        @return A CartesianCoordinate containing the bottom right corner point of the key value map.
        """

        return self.bot_right_point

    def get_height(self):
        """
        @brief Method used to get the height key value of the map.
        @return A integer containing the height key value of the map.
        """

        return self.get_bot_right_point().y - self.get_top_left_point().y + 1

    def get_width(self):
        """
        @brief Method used to get the width of the key value map.
        @return A integer containing the width of the key value map.
        """

        return self.get_bot_right_point().x - self.get_top_left_point().x + 1

    def get_map_points(self):
        """
        @brief Method used to get all the points stored in the map.
        @return A list containing all the occupied points of the map.
        """

        return self.map.keys()

    def is_occupied(self, coordinate : CartesianCoordinate) -> CartesianCoordinate:
        """
        @brief Checks whether a point is occupied in the key value map.
        @return A boolean containing whether the point is occupied.
        """

        return coordinate in self.get_map_points()

    def update_top_left_point(self, new_point):
        """
        @brief Method used to update the TopLeftPoint.
        @param new_point The point you want to check if it should be the new TopLeftPoint
        @details Updates the TopLeftPoint if the new_point is outside the outer border of the current map on the top left.
        """

        if new_point.x < self.top_left_point.x:
            self.top_left_point = CartesianCoordinate(
                new_point.x, self.top_left_point.y)
        if new_point.y < self.top_left_point.y:
            self.top_left_point = CartesianCoordinate(
                self.top_left_point.x, new_point.y)

    def update_bot_right_point(self, new_point : CartesianCoordinate):
        """
        @brief Method used to update the BotRightPoint.
        @param new_point The point you want to check if it should be the new BotRightPoint.
        @details Updates the BotRightPoint if the new_point is outside the outer border of the current map on the bot right.
        """

        if new_point.x > self.bot_right_point.x:
            self.bot_right_point = CartesianCoordinate(
                new_point.x, self.bot_right_point.y)
        if new_point.y > self.bot_right_point.y:
            self.bot_right_point = CartesianCoordinate(
                self.bot_right_point.x, new_point.y)

    def add_point_cartesian(self, point : CartesianCoordinate, state):
        """
        @brief Method used to add a point to the map.
        @param point The point you want to add to the key value map. (CartesianCoordinate)
        @param state The state of the point you want to add. (PointState)
        """

        self.update_top_left_point(point)
        self.update_bot_right_point(point)
        self.map[point] = state