import sys

def camelcase(line):
   line = line.split()
   capped_line = []
   i = 0
   for word in line:
      capped_line.append(word[:-1] + word[-1].capitalize())
   return ' '.join(capped_line)

a = sys.stdin.readlines()

for line in a:
   print (camelcase(line))