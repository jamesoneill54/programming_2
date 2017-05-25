import sys
from string import punctuation

def sort(tup):
   return tup[1]

vowels = {
	'a': 0,
	'e': 0,
	'i': 0,
	'o': 0,
	'u': 0
}

for line in sys.stdin:
   line = line.strip().split()
   for word in line:
      word = word.strip(punctuation).lower()
      if not word:
         continue
      for letter in word:
         if letter in vowels:
            vowels[letter] += 1

len_largest_int = 0
for n in vowels.values():
   if len(str(n)) > len_largest_int:
      len_largest_int = len(str(n))

for v in sorted(vowels.items(), key = sort, reverse = True):
   print ('{:s} : {:{:d}d}'.format(v[0], v[1], len_largest_int))