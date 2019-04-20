#!/bin/python3

from math import sin, cos, pi
from enum import Enum
import time


class angle_c(Enum):
    radians = 1
    degrees = 2


"""
@brief Class polarCoordinate provides functionality to store and convert a polar coordinate. 
"""
class polarCoordinate:
    """
    @brief The constructor for the polarCoordinate class.
    @param distance The distance to the coordinate from the origin.
    @param angle The angle to the coordinate from the origin.
    @param angleType The type of angle (radians of degrees) (angle_c)
    """

    def __init__(self, distance, angle, angleType):
        self.distance = distance
        if angleType is angle_c.degrees:
            self.angle = angle * pi / 180
        else:
            self.angle = angle
        self.angleType = angleType

    """
    @brief Method used to convert this polar coordinate to a cartesian coordinate.
    @return Two integers containing the x and y position of the coordinate.
    """
    def toCartesian(self):
        x = round(self.distance * cos(self.angle))
        y = round(self.distance * sin(self.angle))
        return x, y
