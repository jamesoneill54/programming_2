import sys

class Score(object):

   def __init__(self, goals=0, points=0):
      self.goals = goals
      self.points = points
      self.total = self.goals * 3 + self.points

   def __str__(self):
      return '{:d} goal(s) and {:d} point(s)'.format(self.goals, self.points)

   def __eq__(self, other):
      return self.total == other.total

   def __gt__(self, other):
      return self.total > other.total

   def __ge__(self, other):
      return self.total >= other.total

   def __iadd__(self, other):
      self.goals += other.goals
      self.points += other.points
      self.total += other.total
      return self

   def __add__(self, other):
      return Score(self.goals + other.goals, self.points + other.points)

   def __sub__(self, other):
      return Score(self.goals - other.goals, self.points - other.points)

   def __isub__(self, other):
      self.goals -= other.goals
      self.points -= other.points
      self.total -= other.points
      return self

   def __mul__(self, n):
      self.goals = self.goals * n
      self.points = self.points * n
      self.total = self.total * n
      return self

   def __rmul__(self, n):
      self.goals = self.goals * n
      self.points = self.points * n
      self.total = self.goals + self.points
      return self

   def __imul__(self, n):
      self.goals *= n
      self.points *= n 
      self.total *= n
      return self