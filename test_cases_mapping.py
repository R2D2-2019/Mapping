from mapping import mapping

def test_mapping_constructor():
    """
    This function tests the constructor of Mapping
    with its default constructor values

    """
    map = mapping()
    assert map.current_location is list
    assert map.new_location is list
    assert map.lidar_data is list
    assert map.robot_movement_x is int or float
    assert map.robot_movement_y is int or float

def test_coordinate():
    """
    Test to see if coordinate is a list
    """
    map = mapping()
    coordinate = map.obstacle_coordinates(40)
    assert isinstance(coordinate, list)

def test_update_robot():
    """
    Test if robot moves in order to expand the map
    """
    map = mapping()
    map.current_location = [10,10]
    map.new_location = [15,15]

    map.expand_map([10,10])
    print(map.current_location)
    assert(map.current_location[0] == 15)
    assert(map.current_location[1] == 15)
    
