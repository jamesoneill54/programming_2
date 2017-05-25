import sys
s1 = sys.argv[1]
s2 = sys.argv[2]

for char in s1:
   if char in s2:
      s2 = s2.replace(char, '1')
   else:
      s2 = s2 + '0'

if '0' in s2:
   print ('False')
else:
   print ('True')