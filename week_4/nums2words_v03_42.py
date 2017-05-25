import sys

numbers = {
	'0' : 'zero',
	'1' : 'one',
   '2' : 'two',
   '3' : 'three',
   '4' : 'four',
   '5' : 'five',
   '6' : 'six',
   '7' : 'seven',
   '8': 'eight',
   '9' : 'nine',
   '10' : 'ten'
}

translation = {}
with open(sys.argv[1], 'r') as f:
   for line in f:
      line = line.strip().split()
      translation[line[0]] = line[1]

for line in sys.stdin:
   line = line.strip().split()
   worded_nums = []
   for num in line:
      worded_nums.append(translation[numbers[num]])
   print (' '.join(worded_nums))