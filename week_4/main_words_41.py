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

d2 = {}
for key in d:
   if len(key) > 3 and d[key] >= 3:
      d2[key] = d[key]

longest_int = len(str(max(d2.values())))
longest_word = len(max(d2.keys(), key = len))

for key in sorted(d2):
   print ('{:>{:d}s} : {:{:d}d}'.format(key, longest_word, d2[key], longest_int))