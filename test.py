from random import randint
from cartesian_coordinate import CartesianCoordinate
from mapping_interface import MapInterface
import time
import sys
from quadtree import quadtree
from quadtree import rectangle

"""
This is file is used to test the speed of quadtree implementation.
The result can be found i https://drive.google.com/file/d/1X6KVtICY1phGaAvjiEj3Fw_467A25GXR.
"""
if __name__ == '__main__':
    total = 0
    # init
    start  = time.perf_counter()

    root_size_rec = rectangle(0, 0, 200, 200)
    qt = quadtree(root_size_rec, 4)

    end = time.perf_counter()
    print("Init 400x400 quadtree: ", end -start)
    total += end -start

    # Insert Points
    random_points = []
    for i in range(500):
        random_points.append(CartesianCoordinate(randint(-200,200),randint(-200,200)))

    start  = time.perf_counter()

    for p in random_points:
        qt.insert(p)

    end = time.perf_counter()
    print("Insert 500 random Points : ", end-start)
    total += end -start
    # # Print Tree info
    # qt.print_tree()
    #

    # Get all points
    start  = time.perf_counter()
    all = qt.getMapPoints()
    end = time.perf_counter()
    print("Get all points(500) : ", end-start)
    total += end -start

    # # # Print the whole map representation in terminal
    # # qt.print_map()
    #
    # Test query, get points from a certain range(part of the map)
    query_points = []
    query_range = rectangle(0,0,50,50)
    start = time.perf_counter()
    qt.query(query_range, query_points)
    end = time.perf_counter()
    print("Get all points from a 100x100 area : ", end-start)
    total += end -start
    #test EXPAND
    start = time.perf_counter()
    qt.expand()
    end = time.perf_counter()
    print("Expand a 400x400(to 800x800) : ", end-start)
    total += end -start
    print("Total : ", total)
