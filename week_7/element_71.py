import sys

class Element(object):

   def __init__(self, number, name, symbol, boiling_point):
      self.number = number
      self.name = name
      self.symbol = symbol
      self.boiling_point = boiling_point

   def print_details(self):
      print ('Number:', str(self.number))
      print ('Name:', str(self.name), )
      print ('Symbol:', str(self.symbol))
      print ('Boiling point:', str(self.boiling_point), 'K')

