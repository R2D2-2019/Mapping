from cartesian_coordinate import CartesianCoordinate
from mapping_interface import MapInterface, PointState

"""
@brief Class ListMap provides functionality to create a map using keys and values. 
"""


class ListMap(MapInterface):
    """
    @brief ListMap constructor used to create a basic list map.
    """

    def __init__(self):
        self.map = [
            [PointState.unoccupied, PointState.unoccupied, PointState.unoccupied],
            [PointState.unoccupied, PointState.unoccupied, PointState.unoccupied],
            [PointState.unoccupied, PointState.unoccupied, PointState.unoccupied]
        ]
        self.origin = CartesianCoordinate(1, 1)
        self.topLeftPoint = CartesianCoordinate(-1, -1)
        self.botRightPoint = CartesianCoordinate(1, 1)

    """
    @brief Method used to get the topLeftPoint of the list map.
    @return A CartesianCoordinate containing the top left corner point of the vector map.
    """

    def getTopLeftPoint(self):
        return self.topLeftPoint

    """
    @brief Method used to get the botRightPoint of the list map.
    @return A CartesianCoordinate containing the bottom right corner point of the vector map.
    """

    def getBotRightPoint(self):
        return self.botRightPoint

    """
    @brief Method used to get the height of the list map.
    @return A integer containing the height list of the map.
    """

    def getHeight(self):
        return len(self.map)

    """
    @brief Method used to get the width of the list map.
    @return A integer containing the width of the list map.
    """

    def getWidth(self):
        return len(self.map[0])

    """
    @brief Method used to get all the points stored in the map.
    @return A dictionary containing all the points of the map.
    """

    def getMapPoints(self):
        return self.map

    """
    @brief Method used to check if the coordinate is valid.
    @return A boolean containing True if valid else False.
    """

    def isValidCoordinate(self, coordinate):
        if coordinate.y > len(self.map) - 1 or coordinate.x > len(self.map[coordinate.y]) - 1:
            return False

    """
    @brief Method used to check if the coordinate is an occupied location
    @return A boolean containing True if occupied else False.	.
    """

    def isOccupied(self, coordinate):
        self.isValidCoordinate(coordinate)
        return self.map[self.origin.y + coordinate.y][self.origin.x + coordinate.x] == PointState.occupied

    """
    @brief Method used to expand the map on the top.
    @details This adds new rows to the map on the top.
    @param amountOfNewRows The amount of rows you want to add to the top.
    @warning This method moves the origin.
    """

    def expandTop(self, amountOfNewRows):
        self.origin.y += amountOfNewRows
        newRow = [PointState.unoccupied for col in self.map[0]]
        for i in range(amountOfNewRows):
            self.map.insert(0, list(newRow))

    """
    @brief Method used to expand the map on the bottom.
    @details This adds new rows to the map on the bottom.
    @param amountOfNewRows The amount of rows you want to add to the bottom.
    """

    def expandBottom(self, amountOfNewRows):
        newRow = [PointState.unoccupied for col in self.map[0]]
        for i in range(amountOfNewRows):
            self.map.insert(len(self.map)-1, list(newRow))

    """
    @brief Method used to expand the map on the left.
    @details This adds new columns to the map on the left.
    @param amountOfNewCols The amount of columns you want to add to the left for each row.
    @warning This method moves the origin.
    """

    def expandLeft(self, amountOfNewCols):
        self.origin.x += amountOfNewCols
        for row in self.map:
            for col in range(amountOfNewCols):
                row.insert(0, PointState.unoccupied)

    """
    @brief Method used to expand the map on the right.
    @details This adds new columns to the map on the right.
    @param amountOfNewCols The amount of columns you want to add to the right for each row.
    """

    def expandRight(self, amountOfNewCols):
        for row in self.map:
            for col in range(amountOfNewCols):
                row.insert(len(row) - 1, PointState.unoccupied)

    """
    @brief Method used to update the TopLeftPoint.
    @param newPoint The point you want to check if it should be the new TopLeftPoint
    @details Updates the TopLeftPoint if the newPoint is outside the outer border of the current map on the top left.
    """

    def updateTopLeftPoint(self, newPoint):
        if newPoint.x < self.topLeftPoint.x:
            self.expandLeft(self.topLeftPoint.x - newPoint.x)
            self.topLeftPoint = CartesianCoordinate(
                newPoint.x, self.topLeftPoint.y)
        if newPoint.y < self.topLeftPoint.y:
            self.expandTop(self.topLeftPoint.y - newPoint.y)
            self.topLeftPoint = CartesianCoordinate(
                self.topLeftPoint.x, newPoint.y)

    """
    @brief Method used to update the BotRightPoint.
    @param newPoint The point you want to check if it should be the new BotRightPoint.
    @details Updates the BotRightPoint if the newPoint is outside the outer border of the current map on the bot right.
    """

    def updateBotRightPoint(self, newPoint):
        if newPoint.x > self.botRightPoint.x:
            self.expandRight(newPoint.x - self.botRightPoint.x)
            self.botRightPoint = CartesianCoordinate(
                newPoint.x, self.botRightPoint.y)
        if newPoint.y > self.botRightPoint.y:
            self.expandBottom(newPoint.y - self.botRightPoint.y)
            self.botRightPoint = CartesianCoordinate(
                self.botRightPoint.x, newPoint.y)

    """
    @brief Method used to add a point to the map.
    @param point The point you want to ad	d to the key value map. (CartesianCoordinate)
    @param state The state of the point you want to add. (PointState)
    """

    def addPointCartesian(self, point, state):
        self.updateTopLeftPoint(point)
        self.updateBotRightPoint(point)
        self.map[self.origin.y + point.y][self.origin.x + point.x] = state
