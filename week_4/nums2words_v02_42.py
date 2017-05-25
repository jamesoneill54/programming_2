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

for line in sys.stdin:
   line = line.strip().split()
   worded_nums = []
   for num in line:
      if num in numbers:
         worded_nums.append(numbers[num])
      else:
         worded_nums.append('unknown')   
   print (' '.join(worded_nums))