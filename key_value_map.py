from cartesian_coordinate import CartesianCoordinate
from mapping_interface import MapInterface, PointState

"""
@brief Class keyValueMap provides functionality to create a map using keys and values. 
"""
class keyValueMap(MapInterface):
	"""
	@brief keyValueMap constructor used to create a basic key value map.
	"""
	def __init__(self):
		self.map = {}
		self.topLeftPoint = CartesianCoordinate(0,0)
		self.botRightPoint = CartesianCoordinate(0,0)

	"""
	@brief Method used to get the topLeftPoint of the key value map.
	@return A CartesianCoordinate containing the top left corner point of the key value map.
	"""
	def getTopLeftPoint(self):
		return self.topLeftPoint

	"""
	@brief Method used to get the botRightPoint of the key value map.
	@return A CartesianCoordinate containing the bottom right corner point of the key value map.
	"""
	def getBotRightPoint(self):
		return self.botRightPoint

	"""
	@brief Method used to get the height key value of the map.
	@return A integer containing the height key value of the map.
	"""
	def getHeight(self):
		return self.getBotRightPoint().y - self.getTopLeftPoint().y + 1
	
	"""
	@brief Method used to get the width of the key value map.
	@return A integer containing the width of the key value map.
	"""
	def getWidth(self):
		return self.getBotRightPoint().x - self.getTopLeftPoint().x + 1

	"""
	@brief Method used to get all the points stored in the map.
	@return A list containing all the occupied points of the map.
	"""
	def getMapPoints(self):
		return self.map.keys()
	
	"""
	@brief Checks whether a point is occupied in the key value map. 
	@return A boolean containing whether the point is occupied.
	"""
	def isOccupied(self, coordinate):
		return CartesianCoordinate(coordinate.x, coordinate.y) in self.getMapPoints()

	"""
	@brief Method used to update the TopLeftPoint.
	@param newPoint The point you want to check if it should be the new TopLeftPoint
	@details Updates the TopLeftPoint if the newPoint is outside the outer border of the current map on the top left.
	"""
	def updateTopLeftPoint(self, newPoint):
		if newPoint.x < self.topLeftPoint.x:
			self.topLeftPoint = CartesianCoordinate(newPoint.x, self.topLeftPoint.y)
		if newPoint.y < self.topLeftPoint.y:
			self.topLeftPoint = CartesianCoordinate(self.topLeftPoint.x, newPoint.y)

	"""
	@brief Method used to update the BotRightPoint.
	@param newPoint The point you want to check if it should be the new BotRightPoint.
	@details Updates the BotRightPoint if the newPoint is outside the outer border of the current map on the bot right.
	"""
	def updateBotRightPoint(self, newPoint):
		if newPoint.x > self.botRightPoint.x:
			self.botRightPoint = CartesianCoordinate(newPoint.x, self.botRightPoint.y)
		if newPoint.y > self.botRightPoint.y:
			self.botRightPoint = CartesianCoordinate(self.botRightPoint.x, newPoint.y)

	"""
	@brief Method used to add a point to the map.
	@param point The point you want to add to the key value map. (CartesianCoordinate)
	@param state The state of the point you want to add. (PointState)
	"""
	def addPointCartesian(self, point, state):
		self.updateTopLeftPoint(point)
		self.updateBotRightPoint(point)
		self.map[point] = state
