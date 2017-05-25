import sys
from math import sqrt

class Point(object):

   def __init__(self, x=0, y=0):
      self.x = x
      self.y = y

   def distance(self, other):
      self.distance = sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

   def __str__(self):
      return '({:.01f}, {:.01f})'.format(self.x, self.y)


class Segment(object):

   def __init__(self, p1, p2):
      self.p1 = p1
      self.p2 = p2

   def midpoint(self):
      return Point((self.p1.x + self.p2.x) / 2,  (self.p1.y + self.p2.y) / 2) 

   def length(self):
      return sqrt((self.p2.x - self.p1.x) ** 2 - (self.p2.y - self.p1.y) ** 2)

class Circle(object):

   def __init__(self, centre, radius):
      self.radius = radius
      self.centre = centre

   def overlaps(self, other):
      return sqrt((other.centre.x - self.centre.x) ** 2 + (other.centre.y - self.centre.y) ** 2) < self.radius + other.radius