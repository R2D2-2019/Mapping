from random import randint


class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "(x=%s, y=%s)" % (self.x, self.y)


class rectangle:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def contains(self, point):
        return (point.x >= self.x - self.width and
            point.x <= self.x + self.width and
            point.y >= self.y - self.height and
            point.y <= self.y + self.height)


class quadtree:
    def __init__(self,boundary,capacity):
        self.boundary = boundary
        self.capacity = capacity
        self.points = []
        self.divided = False

    def insert(self,point):
        if (not self.boundary.contains(point)):
            return

        if(self.capacity > len(self.points)):
            self.points.append(point)
        else:
            if not self.divided:
                print ("subdivide")
                self.subdivide()

            self.topleft.insert(point)
            self.topright.insert(point)
            self.bottomleft.insert(point)
            self.bottomright.insert(point)

    def subdivide(self):
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

    def print_tree(self, rootnumber = 0, treename = "root"):
        if len(self.points) > 0:
            print ("Rootdepth = ", rootnumber,
                    "position = ", treename,
                    "points = ", len(self.points))
            for p in self.points:
                print(p)
        else:
            return

        if self.divided:
            self.topleft.print_tree(rootnumber + 1,"topleft")
            self.topright.print_tree(rootnumber + 1,"topright")
            self.bottomleft.print_tree(rootnumber + 1,"bottomleft")
            self.bottomright.print_tree(rootnumber + 1,"bottomright")
        print()


if __name__ == '__main__':
    print ("hello world")

    root_size_rec = rectangle(100,100,100,100)
    qt = quadtree(root_size_rec,4)

    ppes = []
    counter = 0;
    for i in range(10):
        p = point(randint(0,200), randint(0,200))
        qt.insert(p)
        counter += 1
        ppes.append(p)

    print("TOTAL : ", counter)
    print("POINTS: ", ppes)
    qt.print_tree()

"TODO: Make show/print function for quadtree"
