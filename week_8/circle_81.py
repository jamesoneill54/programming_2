import sys

class Point(object):

   def __init__(self, x=0, y=0):
      self.x = x
      self.y = y

   def midpoint(self, other):
      return Point((self.x + other.x) / 2, (self.y + other.y) / 2)

   def __str__(self):
      return '({:0.1f}, {:0.1f})'.format(self.x, self.y)


class Circle(object):

   def __init__(self, centre=Point(), radius=0):
      self.radius = radius
      self.centre = centre

   def __str__(self):
      return 'Centre: {:}\nRadius: {:}'.format(self.centre, self.radius)

   def __add__(self, other):
      return Circle(self.centre.midpoint(other.centre), self.radius + other.radius)