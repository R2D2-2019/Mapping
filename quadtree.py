from random import randint

"""
@package Quadtree
This module is the implementation of mapping using quadtree algorithm.
"""

class point:
    """
    @brief A point class that contains x and y.
    """
    def __init__(self,x,y):
        """
        @brief The constructor.
        @param x The x coordinate of the point(width)
        @param y The x coordinate of the point(height)
        """
        self.x = x
        self.y = y

    def __repr__(self):
        """
        @brief The __repr__ used to represent the point(helps with print function).
        @return A string containing x and y.
        """
        return "(x=%s, y=%s)" % (self.x, self.y)

    def __eq__(self, other):
        """
        @brief Equal comparator.
        @param other The other point that the point will be compared to.
        @return Boolean
        """
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        """
        @brief NOt Equal comparator.
        @param other The other point that the point will be compared to.
        @return Boolean
        """
        return self.x != other.x or self.y != other.y

class rectangle:
    """
    @brief A rectangle that contans the size of the root/tree/subtree.
    """
    def __init__(self,x,y,w,h):
        """
        @brief The constructor.
        @param x The x coordinate of the middle point of the rectangle(width).
        @param y The x coordinate of the middle point of the rectangle(height).
        @param w The width of the rectangle(left and right from the middle point).
        @param h The height of the rectangle(above and below from the middle point).
        """
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def contains(self, point):
        """
        @brief A function to check if a point position is inside the rectangle area.
        @return Boolean.
        """
        return (point.x >= self.x - self.width and
            point.x <= self.x + self.width and
            point.y >= self.y - self.height and
            point.y <= self.y + self.height)

    def intersects(self, other):
        return not((other.x - other.width > self.x + self.width) or
        (other.x + other.width < self.x - self.width) or
        (other.y - other.height > self.y + self.height) or
        (other.y + other.height < self.y - self.height))


class quadtree:
    """
    @brief A tree node that can divide in 4 smaller nodes. First is root.
    """
    def __init__(self,boundary,capacity):
        """
        @brief The constructor.
        @param boundary The quadtree size/boundary(a rectangle class).
        @param capacity The maximal capacity of the tree node before it has to subdivide.
        """
        self.boundary = boundary
        self.capacity = capacity
        self.points = []
        self.divided = False

    def insert(self,point):
        """
        @brief Insert function to insert a point into the quadtree.
        @param point The point that will be inserted into the quadtree(point class).
        @return Boolean. Wether the points was inserted or not, The point position must be inside the tree's area.
        """
        if (not self.boundary.contains(point)):
            return False

        if(self.capacity > len(self.points)):
            self.points.append(point)
            return True

        if not self.divided:
            print ("subdivide")
            self.subdivide()

        return self.topleft.insert(point) or self.topright.insert(point) or self.bottomleft.insert(point) or self.bottomright.insert(point)

    def subdivide(self):
        """
        @brief Subdivides the quadtree node into four smaller treenodes.
        """
        x = self.boundary.x
        y = self.boundary.y
        w = self.boundary.width / 2
        h = self.boundary.height / 2

        tr = rectangle(x+w, y-h, w, h)
        self.topright = quadtree(tr, self.capacity)

        tl = rectangle(x-w, y-h, w, h)
        self.topleft = quadtree(tl, self.capacity)

        br = rectangle(x+w, y+h, w, h)
        self.bottomright = quadtree(br, self.capacity)

        bl = rectangle(x-w, y+h, w, h)
        self.bottomleft = quadtree(bl, self.capacity)

        self.divided = True

    def query(self, selected_range, found):
        """
        @brief A function to get a part of the map, by giving a specific range.
        @param range A rectangle that describes the area u want to know its points.
        @param[out] found An array variable to receive all the points found in the query range.
        """
        if not self.boundary.intersects(selected_range):
            return found;

        for p in self.points:
            if selected_range.contains(p):
                found.append(p)

        if self.divided:
            self.topleft.query(selected_range,found)
            self.topright.query(selected_range,found)
            self.bottomleft.query(selected_range,found)
            self.bottomright.query(selected_range,found)

        return

    def get_points(self, all_points):
        """
        @brief A function to get all the points from the quadtree.
        @param[out] An array/container to return the points in.
        """
        for p in self.points:
            all_points.append(p)

        if self.divided:
            self.topleft.get_points(all_points)
            self.topright.get_points(all_points)
            self.bottomleft.get_points(all_points)
            self.bottomright.get_points(all_points)

    def print_tree(self, rootnumber = 0, treename = "root"):
        """
        @brief Print the tree information, mainly used for debuging/developing.
        @param rootnumber The depth of the three node.
        @param treename The name/position of the quadtree node.
        """
        if len(self.points) > 0:
            print ("Rootdepth = ", rootnumber,
                    ", position = ", treename,
                    ", points = ", len(self.points))
            for p in self.points:
                print(p)
        else:
            return

        if self.divided:
            self.topleft.print_tree(rootnumber + 1,treename + " topleft")
            self.topright.print_tree(rootnumber + 1,treename + " topright")
            self.bottomleft.print_tree(rootnumber + 1,treename + " bottomleft")
            self.bottomright.print_tree(rootnumber + 1,treename + " bottomright")
        print()

    def print_map(self):
        """
        @brief A function to print the map using basic ASCII.
        """
        x_start = self.boundary.x - self.boundary.width
        x_end = self.boundary.x + self.boundary.width
        y_start = self.boundary.y - self.boundary.height
        y_end = self.boundary.y + self.boundary.height

        all_points = []
        self.get_points(all_points)

        for x in range(x_start, x_end):
            for y in range(y_start, y_end):
                if point(x,y) in all_points:
                    print("#", end="")
                else:
                    print("-",end="")
            print()
        return

    def print_query(self, selected_range, found):
        """
        @brief A function to print the selected part of the map using basic ASCII.
        """
        x_start = selected_range.x - selected_range.width
        x_end = selected_range.x + selected_range.width
        y_start = selected_range.y - selected_range.height
        y_end = selected_range.y + selected_range.height

        for x in range(x_start, x_end):
            for y in range(y_start, y_end):
                if point(x,y) in found:
                    print("#", end="")
                else:
                    print("-",end="")
            print()
        return


if __name__ == '__main__':
    #init
    root_size_rec = rectangle(100,100,100,100)
    qt = quadtree(root_size_rec,4)

    #Insert Points
    for i in range(200):
        p = point(randint(0,200), randint(0,200))
        qt.insert(p)

    #Print Tree info
    qt.print_tree()

    #Get all points
    all = []
    qt.get_points(all)
    print(all)

    #Print the map representation in terminal
    qt.print_map()

    #test query, get points from a certain range
    query_points = []
    query_range = rectangle(0,200,20,20)
    qt.query(query_range, query_points)
    qt.print_query(query_range, query_points)

"TODO:Reconstruct subdivide, maybe split main"
