import sys
from math import sqrt

def quadratic_roots(a, b, c):
   inroot = (b ** 2) - (4 * a * c)
   if inroot < 0:
      return None
   r1 = (-b + sqrt(inroot)) / (2 * a)
   r2 = (-b - sqrt(inroot)) / (2 * a)
   return [r1, r2]

def main():
   for line in sys.stdin:
      a, b, c = line.strip().split()
      out = quadratic_roots(float(a), float(b), float(c))
      if out:
         print('r1 =', str(out[0]) + ', r2 =', str(out[1]))
      else:
         print(out)
 
if __name__ == '__main__':
   main()