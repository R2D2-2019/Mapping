from cartesian_coordinate import CartesianCoordinate
from enum import Enum


class PointState(Enum):
    """
    @brief PointState enum used to determine what the state of a location is.
    """

    unoccupied = 0, "unoccupied"
    occupied = 1, "occupied"

    def __new__(cls, value, name):
        """
        @brief PointState enum used to determine what the state of a location is.
        @details 
        This method creates a new instance of the PointState class
        and sets the value and name.
        @param value The value of the PointState you want to set to the new PointState.
        @param name The name of the PointState you want to set to the new PointState.
        @return A new PointState object containing the given value and name. 
        """

        member = object.__new__(cls)
        member._value_ = value
        member.__name__ = name
        return member

    def __int__(self):
        """
        @brief Used to cast the object to an int.
        @details Returns the value of the class when int() is called.
        @return Integer containing the value of the object.
        """

        return self.value


class MapInterface():
    """
    @brief Base class used to create multiple map implementations.
    """

    def get_top_left_point(self):
        """
        @brief Pure virtual method used to get the top left point of a map.
        @return A CartesianCoordinate containing the top left corner point of a map.
        @warning This method must be overridden.
        """

        raise NotImplementedError()

    def get_bot_right_point(self):
        """
        @brief Pure virtual method used to get the bottom right point of a map.
        @return A CartesianCoordinate containing the top left corner point of a map.
        @warning This method must be overridden.
        """

        raise NotImplementedError()

    def get_height(self):
        """
        @brief Pure virtual method used to get the height of a map.
        @return A integer containing the height of a map.
        @warning This method must be overridden.
        """

        raise NotImplementedError()

    def get_width(self):
        """
        @brief Pure virtual method used to get the width of a map.
        @return A integer containing the width of a map.
        @warning This method must be overridden.
        """

        raise NotImplementedError()

    def get_map_points(self):
        """
        @brief Pure virtual method used to get all the occupied points stored in a map.
        @return A dictionary containing all the points of a map.
        @warning This method must be overridden.
        """

        raise NotImplementedError()

    def is_occupied(self, coordinate):
        """
        @brief Pure virtual method used to check if a location is occupied in a map.
        @return A boolean containing whether the location is occupied or not.
        @warning This method must be overridden.
        """

        raise NotImplementedError()

    def __str__(self):
        """
        @brief Method used to return a visual representation of a map in a string.
        @return A string containing a visual representation of a map.
        """

        result = str()
        points = self.get_map_points()
        for h in range(self.get_height() - 1, -1, -1):
            for w in range(self.get_width()):
                if CartesianCoordinate(self.get_top_left_point().x + w, self.get_top_left_point().y + h) in points:
                    result += 'x'
                else:
                    result += '-'
            result += '\n'
        return result
