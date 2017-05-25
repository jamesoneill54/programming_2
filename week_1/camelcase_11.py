import sys

def camelcase(line):
   line = line.split()
   capped_line = []
   for word in line:
      capped_line.append(word.capitalize())
   return ' '.join(capped_line)
   
a = sys.stdin.readlines()

for line in a:
   print (camelcase(line))