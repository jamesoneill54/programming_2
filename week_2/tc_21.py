import sys

def token_count(line, count):
   line = line.split()
   count += len(line)
   return count

def main():
   count = 0
   for line in sys.stdin:
      count = token_count(line, count)
   print (count)

if __name__ == '__main__':
   main()