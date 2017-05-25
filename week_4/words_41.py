import sys
from string import punctuation

d = {}

for line in sys.stdin:
   words = line.strip().split()
   for w in words:
      w = w.strip(punctuation).lower()
      if w in d:
         d[w] += 1
      else: 
         d[w] = 1

for key in sorted(d):
   print (key, ':', d[key])