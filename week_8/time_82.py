import sys

class Time(object):

   def __init__(self, hour=0, minute=0, second=0):
      self.hour = hour
      self.minute = minute
      self.second = second

   def time_to_seconds(self):
      return self.hour * 60 * 60 + self.minute * 60 + self.second

   def seconds_to_time(s):
      minute, second = divmod(s, 60)
      hour, minute = divmod(minute, 60)
      excess, hour = divmod(hour, 24)
      return Time(hour, minute, second)

   def __str__(self):
      return 'The time is {:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second)

   def __eq__(self, other):
      return self.time_to_seconds() == other.time_to_seconds()

   def __gt__(self, other):
      return self.time_to_seconds() > other.time_to_seconds()

   def __add__(self, other):
      total = self.time_to_seconds() + other.time_to_seconds()
      return Time.seconds_to_time(total)

   def __iadd__(self, other):
      total = self.time_to_seconds() + other.time_to_seconds()
      minute, self.second = divmod(total, 60)
      hour, self.minute = divmod(minute, 60)
      excess, self.hour = divmod(hour, 24)
      return self