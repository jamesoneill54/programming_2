import sys

def sumFac(n):
   total_of_factors = 0
   for x in range(1, int(n / 2) + 1):
      if n % x == 0:
         total_of_factors += x
   return total_of_factors

def isPerfect(n):
   return sumFac(n) == n

def main():
   for line in sys.stdin:
      print (isPerfect(int(line.strip())))

if __name__ == '__main__':
   main()