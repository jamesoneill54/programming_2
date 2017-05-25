import sys

units = {
   '0' : 'zero',
   '1' : 'one',
   '2' : 'two',
   '3' : 'three',
   '4' : 'four',
   '5' : 'five',
   '6' : 'six',
   '7' : 'seven',
   '8' : 'eight',
   '9' : 'nine',
}

teens = {
   '10' : 'ten',
   '11' : 'eleven',
   '12' : 'twelve',
   '13' : 'thirteen',
   '14' : 'fourteen',
   '15' : 'fifteen',
   '16' : 'sixteen',
   '17' : 'seventeen',
   '18' : 'eighteen',
   '19' : 'nineteen',
}

higher = {
   '2' : 'twenty',
   '3' : 'thirty',
   '4' : 'forty',
   '5' : 'fifty',
   '6' : 'sixty',
   '7' : 'seventy',
   '8' : 'eighty',
   '9' : 'ninety',
   '10' : 'one hundred'
}

for line in sys.stdin:
   line = line.strip().split()
   worded_nums = []
   for number in line:
      if len(number) == 1:
         worded_nums.append(units[number])
      elif number in teens:
         worded_nums.append(teens[number])
      elif number[-1] == '0':
         worded_nums.append(higher[number[0:-1]])
      else:
         worded_nums.append('{:s}-{:s}'.format(higher[number[0]], units[number[-1]]))
   print (' '.join(worded_nums))