import sys
s = sys.argv[1]

if len(s) >= 2:
   print (s[:-1].capitalize() + s[-1].upper())