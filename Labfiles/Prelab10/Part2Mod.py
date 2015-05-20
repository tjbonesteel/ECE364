#! /usr/bin/env python

import sys
import os
import math

class Point3D:
	def __init__(self, x=0.0, y=0.0, z=0.0):
		self.x = float(x)
                self.y = float(y)
                self.z = float(z)
		
	def distance_from(self, other):
		
                xsq = (self.x - other.x) * (self.x - other.x)
                ysq = (self.y - other.y) * (self.y - other.y)
                zsq = (self.z - other.z) * (self.z - other.z)
                return math.sqrt(xsq + ysq+ zsq)

	def nearest_point(self, points):
		dist = 10000000
                closest = 0
                for item in points:
                        pdist = distance_from(points[item])
                        if pdist < dist:
                                closest = item
                return points[closest]
                                
		
	def clone(self):
		# Put code here
		
	def __str__(self):
		# Converts this object to a string representation
		# Called when you convert this object to a string with str()
		return "(%.3f, %.3f, %.3f)" % (self.x, self.y, self.z)
				
class PointSet:
	def __init__(self):
		
		
	def add_point(self, p):
		# Put code here
		
	def get_num_points(self):
		# Put code here
		
	def compute_bounding_box(self):
		# Put code here
		
	def compute_nearest_neighbors(self, other_point_set):
		# Put code here
			
	
				
