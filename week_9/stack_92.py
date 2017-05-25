import sys

class Stack(object):

   def __init__(self):
      self.list = []

   def push(self, e):
      self.list.append(e)
      return self

   def pop(self):
      return self.list.pop(-1)

   def top(self):
      return self.list[-1]

   def is_empty(self):
      return len(self.list) == 0

   def __len__(self):
      return len(self.list)