import sys
from math import sqrt

def standard_deviation(numbers):
   mean = sum(numbers) / len(numbers)
   summation = 0
   for n in numbers:
      summation += (n - mean) ** 2
   try:
      stand_dev = sqrt((1 / (len(numbers) - 1)) * summation)
      return 'Standard deviation: {:.3f}'.format(stand_dev)
   except ZeroDivisionError:
      return 'Standard deviation: NaN'

def main():
   numbers = []
   for line in sys.stdin:
      numbers.append(int(line.strip()))
   print (standard_deviation(numbers))

if __name__ == '__main__':
   main()