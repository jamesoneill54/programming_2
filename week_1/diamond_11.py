import sys

n = int(sys.argv[1])
lead_spaces = n - 1
i = 1
while i < n * 2:
   print (abs(lead_spaces) * ' ', end = '')
   print ((n - abs(lead_spaces) - 1) * '* ', end = '') 
   print ('*')
   lead_spaces -= 1
   i += 1