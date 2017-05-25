import sys

class BankAccount(object):

   next_account_number = 16555232

   def __init__(self, forename, surname, balance):
      self.forename = forename
      self.surname = surname
      self.balance = balance
      self.account_number = BankAccount.next_account_number
      BankAccount.next_account_number += 1

   def lodge(self, lodgement):
      self.balance += lodgement
      return self

   def __str__(self):
      return 'Name: {:s} {:s}\nAccount number: {:d}\nBalance: {:.02f}\n'.format(self.forename, self.surname, self.account_number,
                                                                               self.balance)

class CurrentAccount(BankAccount):

   overdraft = -1000
   account_type = 'current'

   def __init__(self, forename, surname, balance):
      super().__init__(forename, surname, balance)
      self.account_type = CurrentAccount.account_type

   def withdraw(self, withdrawal):
      if self.balance - withdrawal < CurrentAccount.overdraft:
         return print ('Insufficient funds available')
      self.balance -= withdrawal
      return self

   def __str__(self):
      return '{:s}Account type: {:s}'.format(super().__str__(), self.account_type)


class SavingsAccount(BankAccount):

   interest_rate = 0.01
   account_type = 'savings'

   def __init__(self, forename, surname, balance):
      super().__init__(forename, surname, balance)
      self.account_type = SavingsAccount.account_type

   def apply_interest(self):
      self.balance *= (1 + SavingsAccount.interest_rate)
      return self

   def withdraw(self, withdrawal):
      if self.balance < withdrawal:
         return print ('Insufficient funds available')
      self.balance -= withdrawal
      return self

   def __str__(self):
      return '{:s}Account type: {:s}'.format(super().__str__(), self.account_type) 