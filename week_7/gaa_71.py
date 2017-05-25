import sys

class Score(object):

   def __init__(self, goals = 0, points = 0):
      self.goals = goals
      self.points = points
      self.total = goals * 3 + points

   def greater_than(self, other):
      return self.total > other.total

   def less_than(self, other):
      return self.total < other.total

   def equal_to(self, other):
      return self.total == other.total 