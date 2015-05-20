#! /usr/bin/env python2.6

import sys

try:
    from Shape import *
except Exception as e:
    print "Error when importing Shape module:", e
    sys.exit(1)

print "Constructing a simple Polygon"
p = None
try:
    p = Polygon(((3,4),(4,5),(8,10),(1,2)))
except Exception as e:
    print "Error when constructing a Polygon", e

if p:
    print "Attempting to calculate bounding box for Polygon"
    try:
        val = p.calcBoundingBox()
        print "Bounding box is:", val
    except Exception as e:
        print "Error when calculating bounding box for Polygon:", e

print "Constructing a Triangle"
t = None
try:
    t = Triangle(((3,4),(4,5),(6,2)))
except Exception as e:
    print "Error when constructing a Polygon", e

if t:
    print "Attempting to calculate bounding box for Triangle"
    try:
        val = t.calcBoundingBox()
        print "Bounding box is:", val
    except Exception as e:
        print "Error when calculating bounding box for Triangle:", e

    print "Attempting to calculate area for Triangle"
    try:
        val = t.calcArea()
        print "Area is:", val
    except Exception as e:
        print "Error when calculating area for Triangle:", e

print "Constructing a Square"
s = None
try:
    s = Square(((3,4),(3,9),(8,4), (8,9)))
except Exception as e:
    print "Error when constructing a Square", e

if s:
    print "Attempting to calculate bounding box for Square"
    try:
        val = s.calcBoundingBox()
        print "Bounding box is:", val
    except Exception as e:
        print "Error when calculating bounding box for Square:", e

    print "Attempting to calculate area for Square"
    try:
        val = s.calcArea()
        print "Area is:", val
    except Exception as e:
        print "Error when calculating area for Square:", e
        

print "Constructing a Circle"
c = None
try:
    c = Circle((3,4), 5)
except Exception as e:
    print "Error when constructing a Circle", e

if c:
    print "Attempting to calculate bounding box for Circle"
    try:
        val = c.calcBoundingBox()
        print "Bounding box is:", val
    except Exception as e:
        print "Error when calculating bounding box for Circle:", e

    print "Attempting to calculate area for Circle"
    try:
        val = c.calcArea()
        print "Area is: %.2f" % (val,)
    except Exception as e:
        print "Error when calculating area for Circle:", e

print "Constructing a CompoundShape - This will only work if all other classes work"
cs = None
try:
    cs = CompoundShape((p, t, s, c))
except Exception as e:
    print "Error when constructing a CompoundShape", e

if cs:
    print "Attempting to calculate bounding box for CompoundShape"
    try:
        val = cs.calcBoundingBox()
        print "Bounding box is:", val
    except Exception as e:
        print "Error when calculating bounding box for CompoundShape:", e
