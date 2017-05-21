# Support Python 2 and 3




import os
import sys
from copy import deepcopy

from odpslides.namespace import XMLNS_STR, force_to_short, force_to_tag
from odpslides.segments import segment_intersect, Point

EPSILON = 0.01 # threshold for testing Blockade equality

class Blockade(object):
    """
    A Vertical or Horizontal barrier that draw:frame objects can not escape
    """
    
    def __init__(self, p0, p1):
        """
        p0 and p1 are the endpoints, each is off the page, that define the Blockade
        
        Force Blockade to be horizontal or vertical by checking x,y values
        """
        
        dx = abs(p0.x - p1.x)
        dy = abs(p0.y - p1.y)
        if dx > dy: # ...VERY LOOSE on the definition of horizontal and vertical
            self.direction = 'horiz'
            y = (p0.y + p1.y) / 2.0
            p0 = Point( p0.x, y)
            p1 = Point( p1.x, y)
        else:
            self.direction = 'vert'
            x = (p0.x + p1.x) / 2.0
            p0 = Point( x, p0.y)
            p1 = Point( x, p1.y)
        
        self.p0 = p0
        self.p1 = p1
        
        self.segment = (p0, p1) # segment defined by end points
    
    def desc(self):
        if self.direction=='horiz':
            return 'H(%.2f)'%self.p0.y
        else:
            return 'V(%.2f)'%self.p0.x
    
    def __eq__(self, other):
        if (self.direction=='horiz') and (other.direction=='horiz') and abs(self.p0.y-other.p0.y)<=EPSILON:
            return True
            
        if (self.direction=='vert') and (other.direction=='vert') and abs(self.p0.x-other.p0.x)<=EPSILON:
            return True
            
        return False
        
    def set_new_x_value(self, x):
        self.p0.x = x
        self.p1.x = x
        self.segment = (self.p0, self.p1)
        
    def set_new_y_value(self, y):
        self.p0.y = y
        self.p1.y = y
        self.segment = (self.p0, self.p1)
        
    def intersects(self, blockade):
        return segment_intersect(self.segment, blockade.segment)
        
    def get_intersect_pt(self, seg):
        """If there's an intersection, then seg is opposite direction (vert or horiz)"""
        if segment_intersect(self.segment, seg):
            if self.direction == 'vert':
                x_int = self.p0.x
                y_int = seg[0].y
            else:
                x_int = seg[0].x
                y_int = self.p0.y
            return Point( x_int, y_int )
        else:
            return None
    
    def intersects_segment(self, seg):
        return segment_intersect(self.segment, seg)
    
    def __str__(self):
        return 'Blockade(%s) <p0=%s,  p1=%s>'%(self.direction, self.p0, self.p1 )

if __name__=="__main__":
    
    p0a = Point( 0., 0.)
    p0b = Point( 2., 0.)
    p1a = Point( 1., -1.)
    p1b = Point( 1., 1.)
    
    b1 = Blockade(p0a, p0b)
    b2 = Blockade(p1a, p1b)
    
    
    def test_int(block1, block2):
        print('Blockade 1 =', block1)
        print('Blockade 2 =', block2)
        print('intersect =',block1.intersects( block2 ) )
        print('.'*77)
        
        
    print()
    test_int( b1, b2 )
    print( b1.get_intersect_pt( b2.segment ) )
    