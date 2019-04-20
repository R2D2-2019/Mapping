from cartesian_coordinate import CartesianCoordinate
from enum import Enum

class PointState(Enum):
    unoccupied = 0, "unoccupied"
    occupied = 1, "occupied"

    def __new__(cls, value, name):
        member = object.__new__(cls)
        member._value_ = value
        member.__name__ = name
        return member

    def __int__(self):
        return self.value

class MapInterface():
    """
    @brief Pure virtual method used to get the topLeftPoint of a map.
    @return A CartesianCoordinate containing the top left corner point of a map.
    @warning This method must be overridden.	
    """
    def getTopLeftPoint(self):
        raise NotImplementedError()

    """
    @brief Pure virtual method used to get the botRightPoint of a map.
    @return A CartesianCoordinate containing the top left corner point of a map.
    @warning This method must be overridden.
    """
    def getBotRightPoint(self):
        raise NotImplementedError()

    """
    @brief Pure virtual method used to get the height of a map.
    @return A integer containing the height of a map.
    @warning This method must be overridden.	
    """
    def getHeight(self):
        raise NotImplementedError()

    """
    @brief Pure virtual method used to get the width of a map.
    @return A integer containing the width of a map.
    @warning This method must be overridden.	
    """
    def getWidth(self):
        raise NotImplementedError()

    """
    @brief Pure virtual method used to get all the occupied points stored in a map.
    @return A dictionary containing all the points of a map.
    @warning This method must be overridden.		
    """
    def getMapPoints(self):
        raise NotImplementedError()

    """
    @brief Pure virtual method used to check if a location is occupied in a map.
    @return A boolean containing whether the location is occupied or not.
    @warning This method must be overridden.
    """
    def isOccupied(self, coordinate):
        raise NotImplementedError()

    """
    @brief Method used to return a visual representation of a map in a string.
    @return A string containing a visual representation of a map.
    """
    def __str__(self):
        result = str()
        points = self.getMapPoints()
        print(points)
        for h in range(self.getHeight()):
            for w in range(self.getWidth()):
                if CartesianCoordinate(self.getTopLeftPoint().x + w, self.getTopLeftPoint().y + h) in points:
                    result += 'x'
                else:
                    result += '-'
            result += '\n'
        return result