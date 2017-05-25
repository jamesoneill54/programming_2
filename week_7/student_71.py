import sys

class Student(object):

   def __init__(self, surname, forename, sid, modlist = None):
      if not modlist:
         self.modlist = []
      else:
         self.modlist = modlist
      self.surname = surname
      self.forename = forename
      self.sid = sid

   def add_module(self, module):
      if module not in self.modlist:
         self.modlist.append(module)

   def del_module(self, module):
      if module in self.modlist:
         self.modlist.remove(module)

   def print_details(self):
      print ('ID:', self.sid)
      print ('Surname:', self.surname)
      print ('Forename:', self.forename)
      print ('Modules:', ' '.join(self.modlist))