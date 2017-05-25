from collections import namedtuple

Module = namedtuple('Module', 'code title ects')

CA1_MODULES = {'CA103': Module('CA103', 'Computer Systems', 5),
               'CA106': Module('CA106', 'Web Design', 5),
               'CA115': Module('CA115', 'Digital Innovation', 5),
               'CA116': Module('CA116', 'Computer Programming I', 10),
               'CA117': Module('CA117', 'Computer Programming II', 10),
               'CA169': Module('CA169', 'Networks and Internet', 5),
               'CA170': Module('CA170', 'Operating Systems', 5),
               'CA172': Module('CA172', 'Problem Solving', 5),
               'MS121': Module('MS121', 'IT Mathematics', 10)}

class Student(object):

   def __init__(self, idnum, surname, firstname, mods=CA1_MODULES):
      self.__idnum = idnum
      self.__surname = surname
      self.__firstname = firstname
      self.__mods = mods
      self.__marks = {code: 0 for code in self.__mods.keys()}

   def __str__(self):
      name = '{} : {} {}'.format(self.__idnum,
                                 self.__firstname, 
                                 self.__surname)
      
      uline = '-' * len(name)
      results =  '\n'.join([code + ' : ' + self.__mods[code].title + ' : ' + str(self.__marks[code]) for code in sorted(self.__mods.keys())])
      pm = 'Precision mark: {:.2f}'.format(self.precision_mark())
      
      if self.passed():
         outcome = 'Pass'
      
      elif self.passed_by_compensation():
         outcome = 'Pass by compensation'
      
      else:
         outcome = 'Fail'

      return '\n'.join([name, uline, results, pm, outcome])

   
   def add_mark(self, mod_code, mark):
      self.__marks[mod_code] = mark
      return self

   def precision_mark(self):
      total_weight = 0
      awarded_marks = 0
      for key in self.__mods:
         weight = self.__mods[key].ects
         total_weight += weight
         awarded_marks += ((self.__marks[key] / 100) * weight)
      average_percentage = (awarded_marks / total_weight) * 100
      return average_percentage

   def passed(self):
      for key in self.__marks:
         if self.__marks[key] < 40:
            return False
      return True

   def passed_by_compensation(self):
      if self.precision_mark() < 45:
         return False
      mod_percent = 0
      weight = 0
      total_weight = 0
      awarded_marks = 0
      for code in self.__marks:
         mod_percent = self.__marks[code]
         if mod_percent < 35:
            return False
         weight = self.__mods[code].ects
         total_weight += weight
         if mod_percent >= 40:
            awarded_marks += weight
      if (awarded_marks / total_weight) < (5 / 6):
         return False
      return True