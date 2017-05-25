class Employee(object):

   def __init__(self, name, number):
      self.name = name
      self.number = number

   def wages(self):
      return 0

   def __str__(self):
      return 'Name: {:s}\nNumber: {:d}\nWages: {:.2f}'.format(self.name, self.number, self.wages())


class Manager(Employee):

   def __init__(self, name, number, salary):
      super().__init__(name, number)
      self.salary = salary

   def wages(self):
      return self.salary / 52


class AssemblyWorker(Employee):

   def __init__(self, name, number, hourly_rate, hours):
      super().__init__(name, number)
      self.hourly_rate = hourly_rate
      self.hours = hours

   def wages(self):
      return self.hourly_rate * self.hours
