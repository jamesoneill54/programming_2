import sys

def l2d(f):
   [keys, values] = f.readlines()
   keys = keys.strip().split()
   values = values.strip().split()
   d = {}
   i = 0
   while i < len(keys):    
      d[keys[i]] = values[i]
      i += 1
   return d

def main():
   l2d(sys.stdin)

if __name__ == '__main__':
   main()