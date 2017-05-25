import sys

class Employee(object):

   next_employee_number = 0

   def __init__(self, name, hours_worked=0, hourly_rate=9.25):
      self.name = name
      self.employee_number = Employee.next_employee_number
      self.hourly_rate = hourly_rate
      self.hours_worked = hours_worked
      Employee.next_employee_number += 1

   def wage(self):
      return self.hours_worked * self.hourly_rate

   def add_hours(self, hours):
      self.hours_worked += hours

   def __str__(self):
      return 'Name: {:s}\nID: {:d}\nHours: {:0.02f}\nRate: {:0.02f}\nWages: {:0.02f}'.format(self.name, self.employee_number, 
                                                                                             self.hours_worked, self.hourly_rate,
                                                                                             self.wage())