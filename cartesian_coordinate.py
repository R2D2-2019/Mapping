class CartesianCoordinate():
    """
    @brief Class CartesianCoordinate provides functionality to store a cartesian coordinate. 
    """

    def __init__(self, x, y):
        """
        @brief The constructor of the CartesianCoordinate class.
        @param x The x point of the coordinate.
        @param y The y point of the coordinate.
        """

        self.x = x
        self.y = y

    def __add__(self, other):
        """
        @brief Add Operator.
        @param other The other point that the point will be added the to this point.
        """

        self.x += other.x
        self.y += other.y

    def __sub__(self, other):
        """
        @brief Substraction operator.
        @param other The other point that the point will be compared to.
        """

        self.x -= other.x
        self.y -= other.y

    def __eq__(self, other):
        """
        @brief Method used to check if both cartesian coordinates are equal.
        @param other The other point you want to compare to this point.
        @return A boolean containing true if the point are equal otherwise false.
        """

        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        """
        @brief Method used to check if both cartesian coordinates are not equal.
        @param other The other point you want to compare to this point.
        @return A boolean containing false if the point are equal otherwise true.
        """

        return not self.__eq__(other)

    def __hash__(self):
        """
        @brief Method used to create a identical hash using x and y.
        @return A identical hash of the cartesian coordinate.
        """

        return hash((self.x, self.y))

    def __repr__(self):
        """
        @brief Method used to create a string of the cartesian coordinate values.
        @return A string containing the values of the cartesian coordinate.
        """

        return "x: " + str(self.x) + " y: " + str(self.y)