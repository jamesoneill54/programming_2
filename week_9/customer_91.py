class Customer(object):

   discount = 0

   def __init__(self, name, balance, addr_line1, addr_line2, addr_line3):
      self.name = name
      self.balance = balance
      self.addr_line1 = addr_line1
      self.addr_line2 = addr_line2
      self.addr_line3 = addr_line3

   def owes(self):
      return self.balance - (self.balance * self.discount)

   def __str__(self):
      return '{:s}\n{:s}\n{:s}\n{:s}\nBalance: {:.2f}\nDiscount: {:d}%\nAmount due: {:.2f}'.format(self.name, self.addr_line1,
                                                                                                   self.addr_line2, self.addr_line3,
                                                                                                   self.balance, int(self.discount * 100),
                                                                                                   self.owes())


class ValuedCustomer(Customer):

   discount = 0.1