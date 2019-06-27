from math import sin,cos,atan2,sqrt,pi

class Algorithms():
    ##  Documentation for decimal_degrees_to_time_degrees
    #   The function asks for a degree value from 0 till 360.
    #   It then returns the Time degrees in a dict. 
    def decimal_degrees_to_time_degrees(self, decimal_degrees):
        assert decimal_degrees >=0 and decimal_degrees <= 360, "decimal degrees is out of scope"
        time_degrees = {"hours": 0, "minutes": 0, "seconds": 0}
        time_degrees["hours"] = int(decimal_degrees)
        time_degrees["minutes"] = int((decimal_degrees - time_degrees["hours"])*60)
        time_degrees["seconds"] = round((decimal_degrees - time_degrees["hours"] - time_degrees["minutes"] / 60) * 3600)
        return time_degrees
    
    ##  Documentation for time_degrees_to_decimal_degrees
    #   The function asks for a dict with a hours value from 0 till 360,
    #   a minutes value from 0 till 59 and a second value from 0 till 59.
    #   If the hours value is 360 it will set the minutes value and seconds value to 0.
    #   It then returns the decimal degrees in a float
    def time_degrees_to_decimal_degrees(self, time):
        assert time["hours"] >= 0 and time["hours"] <= 360, "Time degrees 'hours' is out of scope"
        assert time["minutes"] >= 0 and time["minutes"] < 60 , "Time degrees 'minutes' is out of scope"
        assert time["seconds"] >= 0 and time["seconds"] < 60, "Time degrees 'seconds' is out of scope"
        if time["hours"] == 360:
            time["minutes"] = 0
            time["seconds"] = 0
        return(time["hours"] + time["minutes"]/60 + time["seconds"] / 3600)

    ## Documentation for measure_distance
    #  The function calculates the distance in meters between two world coordinates
    #  It needs the latitude and longtitude from two coordinates to be able to calculate the distance
    #  Longtitude is the Y value from the world
    #  Latitude is the X value from the world
    def measure_distance(self, lat1, lon1, lat2, lon2):
        R = 6378.137  #Radius of earth in KM
        dLat = lat2 * pi / 180 - lat1 * pi / 180
        dLon = lon2 * pi / 180 - lon1 * pi / 180
        a = sin(dLat/2) * sin(dLat/2) + cos(lat1 * pi / 180) * cos(lat2 * pi / 180) * sin(dLon/2) * sin(dLon/2)
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        d = R * c
        return d * 1000; #meters

    ## Documentation for calc_new_coordinate
    #  The function calculates a new coordinate based on the distance that you give 
    #  The distance x and y is in meters
    #  The latitude and longtitude is the coordinate from the robot
    #  This way you can give an obstacle a world coordinate location
    def calculate_new_coordinate(self, latitude, longtitude, distance_y, distance_x):
        R = 6378.137  #Radius of earth in KM
        new_latitude = latitude + (distance_y / R) * (100 / pi)
        new_longtitude = longtitude + (distance_x / R) * (100 / pi)

    ## Documentation for from_lidar_to_coordinate
    #  The function makes from distance and degree, an x and y value.
    #  This is needed to calculate the coordinate from the lidar given value.
    def from_lidar_to_coordinate(self, lidar_degree, distance):
        degree = lidar_degree
        distance_y = sin(degree) * distance
        distance_x = cos(degree) * distance