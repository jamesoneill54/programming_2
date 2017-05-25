import sys

shortest_w_vowels = ''
vowels = 'aeiou'
a = []
for line in sys.stdin:
   a.append(line.strip())

largest_e_count = max([s.strip().count('e') for s in a if 'e' in s.lower()])

print ('Words containing 17 letters:', [s.strip() for s in a if len(s.lower().strip()) == 17])
print ('Words containing 18+ letters:', [s.strip() for s in a if len(s.lower().strip()) > 17])
print ('Shortest word containing all vowels:', min([s.strip() for s in a if all([v in s for v in vowels])], key = len))
print ("Words with 4 a's:", [s.strip() for s in a if s.lower().count('a') == 4])
print ("Words with 2+ q's:", [s.strip() for s in a if s.lower().count('q') >= 2])
print ('Words containing cie:', [s.strip() for s in a if 'cie' in s.lower().strip()])
print ('Anagrams of angle:', [s.strip() for s in a if sorted(s.lower().strip()) == sorted('angle') and s.lower().strip() != 'angle'])
print ('Words ending in iary:', len([s.strip() for s in a if s.lower().strip().endswith('iary')]))
print ('Words with q but no u:', [s.strip() for s in a if 'q' in s.lower() and not 'qu' in s.lower()])
print ("Words with most e's:", [s.strip() for s in a if s.lower().count('e') == largest_e_count])