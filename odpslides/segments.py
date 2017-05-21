# Support Python 2 and 3





"""
Taken from: https://github.com/crm416/point-location/blob/master/geo/shapes.py
      and: http://www.toptal.com/python/computational-geometry-in-python-from-theory-to-implementation
"""

def ccw(A, B, C):
    """Tests whether the turn formed by A, B, and C is ccw"""
    return (B.x - A.x) * (C.y - A.y) > (B.y - A.y) * (C.x - A.x)
    
    
def intersect(a1, b1, a2, b2):
    """Returns True if line segments a1b1 and a2b2 intersect."""
    if a1==a2 or a1==b2 or b1==a2 or b1==b2:
        return True
    return ccw(a1, b1, a2) != ccw(a1, b1, b2) and ccw(a2, b2, a1) != ccw(a2, b2, b1) 
    
def segment_intersect(s1, s2):
    """Wraps (a1,b1) and (a2,b2) into Segment tuples"""
    return intersect( s1[0], s1[1], s2[0], s2[1] )


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __rmul__(self, c):
        return Point(c * self.x, c * self.y)

    def close(self, that, epsilon=0.01):
        return self.dist(that) < epsilon

    def dist(self, that):
        return sqrt(self.sqrDist(that))

    def sqrDist(self, that):
        dx = self.x - that.x
        dy = self.y - that.y
        return dx * dx + dy * dy

    def np(self):
        """Returns the point's Numpy point representation"""
        return [self.x, self.y]
   
class BBox( object ):
    
    def __init__(self, left_x, right_x, top_y, bottom_y):
        
        self.left_x   = left_x
        self.right_x  = right_x
        self.top_y    = top_y
        self.bottom_y = bottom_y
        
    def __str__(self):
        return 'BBox(%s, %s, %s, %s)'%(self.left_x, self.right_x, self.top_y, self.bottom_y)

if __name__=="__main__":
    
    p00 = Point( 0., 0.)
    p11 = Point( 1., 1.)
    p01 = Point( 0., 1.)
    p10 = Point( 1., 0.)
    
    for p in [p00, p11, p01, p10]:
        print(p)
    
    def test_int(a1, b1, a2, b2):
        print('Segment 1 =', a1, b1)
        print('Segment 2 =', a2, b2)
        print('intersect(a1, b1, a2, b2) =',intersect(a1, b1, a2, b2))
        print('.'*77)
        
        
    print()
    test_int( p00, p11, p01, p10 )
    test_int( p00, p01, p11, p10 )
    test_int( p00, p10, p11, p01 )
    test_int( p00, p11, p01, p11 )
        
