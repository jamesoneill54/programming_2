import sys

class BankAccount(object):

   def __init__(self, balance=0):
      self.balance = balance

   def deposit(self, amount):
      self.balance += amount

   def withdraw(self, amount):
      if amount <= self.balance:
         self.balance -= amount
      else:
         print ('Insufficient funds available')

   def __str__(self):
      return 'Your current balance is: {:.02f} euro'.format(self.balance)