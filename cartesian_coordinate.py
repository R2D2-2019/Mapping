"""
@brief Class CartesianCoordinate provides functionality to store a cartesian coordinate. 
"""
class CartesianCoordinate:
    """
    @brief The constructor of the CartesianCoordinate class.
    @param x The x point of the coordinate.
    @param y The y point of the coordinate.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    """
        @brief Add Operator.
        @param other The other point that the point will be added the to this point.
        @return !DOES NOT RETURN!
    """
    def __add__(self, other):
        self.x += other.x
        self.y += other.y

    """
        @brief Substraction operator.
        @param other The other point that the point will be compared to.
        @return !DOES NOT RETURN!
    """
    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y

    """
    @brief Method used to check if both cartesian coordinates are equal.
    @param other The other point you want to compare to this point.
    @return A boolean containing true if the point are equal otherwise false.
    """
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    """
    @brief Method used to check if both cartesian coordinates are not equal.
    @param other The other point you want to compare to this point.
    @return A boolean containing false if the point are equal otherwise true.
    """
    def __ne__(self, other):
        return not self.__eq__(other)

    """
    @brief Method used to create a identical hash using x and y.
    @return A identical hash of the cartesian coordinate.
    """
    def __hash__(self):
        return hash((self.x, self.y)) 

    """
    @brief Method used to create a string of the cartesian coordinate values.
    @return A string containing the values of the cartesian coordinate.
    """
    def __repr__(self):
        return "x: " + str(self.x) + "  y: " + str(self.y)