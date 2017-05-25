import sys

foodstuff = {}
with open(sys.argv[1], 'r') as f:
   for line in f:
      line = line.strip().split()
      foodstuff[line[0:-1]] = int(line[-1])

people = {}
for line in sys.stdin:
   name = ''
   calories = 0
   line = line.strip().split(',')
   for e in line:
      if e in foodstuff:
         calories += foodstuff[e]
      else:
         calories += 100
   people[name] = calories

longest_name = 0
for key in people.keys():
   if len(key) > longest_name:
      longest_name = len(key)

longest_c_count = 0
for val in people.values():
   if len(str(val)) > longest_c_count:
      longest_c_count = len(str(val))

for p in people:
   print('{:{:d}s} : {:{:d}d}'.format(p, longest_name, people[p], longest_c_count))