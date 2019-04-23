#!/bin/python3

from math import sin, cos, pi
from enum import Enum
import time

class angle(Enum):

    radians = 1
    degrees = 2


class polarCoordinate:
    """
    @brief Class polarCoordinate provides functionality to store and convert a polar coordinate. 
    """

    def __init__(self, distance, angle, angle_type):
        """
        @brief The constructor for the polarCoordinate class.
        @param distance The distance to the coordinate from the origin.
        @param angle The angle to the coordinate from the origin.
        @param angle_type The type of angle (radians of degrees) (angle_c)
        """

        self.distance = distance
        if angle_type is angle.degrees:
            self.angle = angle * pi / 180
        else:
            self.angle = angle
        self.angle_type = angle_type

    def to_cartesian(self):
        """
        @brief Method used to convert this polar coordinate to a cartesian coordinate.
        @return Two integers containing the x and y position of the coordinate.
        """

        x = round(self.distance * cos(self.angle))
        y = round(self.distance * sin(self.angle))
        return x, y
