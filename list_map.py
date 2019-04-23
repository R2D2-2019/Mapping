from cartesian_coordinate import CartesianCoordinate
from mapping_interface import MapInterface
from mapping_interface import PointState

class ListMap(MapInterface):
    """
    @brief Class ListMap provides functionality to create a map using keys and values. 
    """

    def __init__(self):
        """
        @brief ListMap constructor used to create a basic list map.
        """

        self.map = [
            [PointState.unoccupied, PointState.unoccupied, PointState.unoccupied],
            [PointState.unoccupied, PointState.unoccupied, PointState.unoccupied],
            [PointState.unoccupied, PointState.unoccupied, PointState.unoccupied]
        ]
        self.origin = CartesianCoordinate(1, 1)
        self.top_left_point = CartesianCoordinate(-1, -1)
        self.bot_right_point = CartesianCoordinate(1, 1)

    def get_top_left_point(self):
        """
        @brief Method used to get the top_left_point of the list map.
        @return A CartesianCoordinate containing the top left corner point of the vector map.
        """

        return self.top_left_point

    def get_bot_right_point(self):
        """
        @brief Method used to get the bot_right_point of the list map.
        @return A CartesianCoordinate containing the bottom right corner point of the vector map.
        """

        return self.bot_right_point

    def get_height(self):
        """
        @brief Method used to get the height of the list map.
        @return A integer containing the height list of the map.
        """

        return len(self.map)

    def get_width(self):
        """
        @brief Method used to get the width of the list map.
        @return A integer containing the width of the list map.
        """

        return len(self.map[0])

    def get_map_points(self):
        """
        @brief Method used to get all the points stored in the map.
        @return A list containing all the points occupied of the map.
        """

        points = list()
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == PointState.occupied:
                    points.append(CartesianCoordinate(
                        x - self.origin.x, y - self.origin.y
                    ))
        return points

    def is_valid_coordinate(self, coordinate):
        """
        @brief Method used to check if the coordinate is valid.
        @return A boolean containing True if valid else False.
        """

        return not (coordinate.y > len(self.map) - 1 or coordinate.x > len(self.map[coordinate.y]) - 1)

    def is_occupied(self, coordinate):
        """
        @brief Method used to check if the coordinate is an occupied location
        @return A boolean containing True if occupied else False..
        """

        self.is_valid_coordinate(coordinate)
        return self.map[self.origin.y + coordinate.y][self.origin.x + coordinate.x] == PointState.occupied

    def expand_top(self, amount_of_new_rows):
        """
        @brief Method used to expand the map on the top.
        @details This adds new rows to the map on the top.
        @param amount_of_new_rows The amount of rows you want to add to the top.
        @warning This method moves the origin.
        """

        self.origin.y += amount_of_new_rows
        newRow = [PointState.unoccupied for col in self.map[0]]
        for i in range(amount_of_new_rows):
            self.map.insert(0, list(newRow))

    def expand_bottom(self, amount_of_new_rows):
        """
        @brief Method used to expand the map on the bottom.
        @details This adds new rows to the map on the bottom.
        @param amount_of_new_rows The amount of rows you want to add to the bottom.
        """

        newRow = [PointState.unoccupied for col in self.map[0]]
        for i in range(amount_of_new_rows):
            self.map.insert(len(self.map)-1, list(newRow))

    def expand_left(self, amount_of_new_cols):
        """
        @brief Method used to expand the map on the left.
        @details This adds new columns to the map on the left.
        @param amount_of_new_cols The amount of columns you want to add to the left for each row.
        @warning This method moves the origin.
        """

        self.origin.x += amount_of_new_cols
        for row in self.map:
            for col in range(amount_of_new_cols):
                row.insert(0, PointState.unoccupied)

    def expand_right(self, amount_of_new_cols):
        """
        @brief Method used to expand the map on the right.
        @details This adds new columns to the map on the right.
        @param amount_of_new_cols The amount of columns you want to add to the right for each row.
        """

        for row in self.map:
            for col in range(amount_of_new_cols):
                row.insert(len(row) - 1, PointState.unoccupied)

    def update_top_left_point(self, new_point):
        """
        @brief Method used to update the top_left_point.
        @param new_point The point you want to check if it should be the new top_left_point
        @details Updates the top_left_point if the new_point is outside the outer border of the current map on the top left.
        """

        if new_point.x < self.top_left_point.x:
            self.expand_left(self.top_left_point.x - new_point.x)
            self.top_left_point = CartesianCoordinate(
                new_point.x, self.top_left_point.y)
        if new_point.y < self.top_left_point.y:
            self.expand_top(self.top_left_point.y - new_point.y)
            self.top_left_point = CartesianCoordinate(
                self.top_left_point.x, new_point.y)

    def update_bot_right_point(self, new_point):
        """
        @brief Method used to update the BotRightPoint.
        @param new_point The point you want to check if it should be the new BotRightPoint.
        @details Updates the BotRightPoint if the new_point is outside the outer border of the current map on the bot right.
        """

        if new_point.x > self.bot_right_point.x:
            self.expand_right(new_point.x - self.bot_right_point.x)
            self.bot_right_point = CartesianCoordinate(
                new_point.x, self.bot_right_point.y)
        if new_point.y > self.bot_right_point.y:
            self.expand_bottom(new_point.y - self.bot_right_point.y)
            self.bot_right_point = CartesianCoordinate(
                self.bot_right_point.x, new_point.y)

    def add_point_cartesian(self, point, state):
        """
        @brief Method used to add a point to the map.
        @param point The point you want to ad	d to the key value map. (CartesianCoordinate)
        @param state The state of the point you want to add. (PointState)
        """

        self.update_top_left_point(point)
        self.update_bot_right_point(point)
        self.map[self.origin.y + point.y][self.origin.x + point.x] = state
