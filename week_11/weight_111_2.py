class Weight(object):

   OUNCES_PER_POUND = 16

   def __init__(self, pounds=0, ounces=0):
      self.pounds = pounds
      self.ounces = ounces

   @classmethod
   def from_ounces(cls, ounces):
      pounds, ounces = divmod(ounces, cls.OUNCES_PER_POUND)
      return cls(pounds, ounces)

   def total_ounces(self):
      return (self.pounds * Weight.OUNCES_PER_POUND) + self.ounces

   def __str__(self):
      return '{:d} pound(s) and {:d} ounce(s)'.format(self.pounds, self.ounces)

   def __eq__(self, other):
      return self.total_ounces() == other.total_ounces()

   def __gt__(self, other):
      return self.total_ounces() > other.total_ounces()

   def __ge__(self, other):
      return self.total_ounces() >= other.total_ounces()