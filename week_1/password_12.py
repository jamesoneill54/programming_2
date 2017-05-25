import sys

lines = sys.stdin.readlines()

for password in lines:
   password = password.strip()
   upper = 0
   lower = 0
   digit = 0
   symbol = 0
   i = 0
   while i < len(password):
      if password[i].isupper():
         upper = 1
      elif password[i].islower():
         lower = 1
      elif password[i].isdigit():
         digit = 1
      else: 
         symbol = 1
      i += 1
   print (upper + lower + digit + symbol)