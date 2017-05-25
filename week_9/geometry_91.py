import sys
from math import sqrt

class Point(object):

   def __init__(self, x, y):
      self.x = x
      self.y = y

   def distance(self, other):
      return sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)


class Shape(object):

   def __init__(self, points):
      self.points = points

   def sides(self):
      i = 0
      sides = []
      while i < len(self.points) - 1:
         sides.append(self.points[i].distance(self.points[i + 1])) 
         i += 1
      sides.append(self.points[i].distance(self.points[0]))
      return sides

   def perimeter(self):
      return sum(self.sides())


class Triangle(Shape):

   def __init__(self, points):
      super().__init__(points)

   def area(self):
      a, b, c = self.sides()
      s = (a + b + c) / 2
      return sqrt(s * (s - a) * (s - b) * (s - c))


class Square(Shape):

   def __init__(self, points):
      super().__init__(points)

   def area(self):
      return self.sides()[0] ** 2