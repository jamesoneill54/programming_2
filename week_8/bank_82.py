import sys

class BankAccount(object):

   next_account_number = 16555232
   total_lodgements = 0
   interest_rate = 0.043

   def __init__(self, forename, surname, balance=float(0)):
      self.forename = forename
      self.surname = surname
      self.balance = balance
      self.account_number = BankAccount.next_account_number
      BankAccount.next_account_number += 1

   def lodge(self, lodgement):
      self.balance += lodgement
      BankAccount.total_lodgements += 1
      return self

   def apply_interest(self):
      self.balance *= (1 + BankAccount.interest_rate)
      return self

   def __iadd__(self, increment):
      self.balance += increment
      BankAccount.total_lodgements += 1
      return self

   def __str__(self):
      return 'Name: {:s} {:s}\nAccount number: {:d}\nBalance: {:0.02f}'.format(self.forename, self.surname, self.account_number, self.balance)