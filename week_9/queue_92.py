import sys

class Queue(object):

   def __init__(self):
      self.list = []

   def enqueue(self, e):
      self.list.append(e)
      return self

   def dequeue(self):
      return self.list.pop(0)

   def first(self):
      return self.list[0]

   def is_empty(self):
      return len(self.list) == 0

   def __len__(self):
      return len(self.list)