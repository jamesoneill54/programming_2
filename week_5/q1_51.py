import sys

def swap_adjacent(s):
   odds = [l for l in s[::2]]
   evens = [l for l in s[1::2]]
   swapped = ''
   i = 0
   while i < len(odds) or i < len(evens):
      if i < len(evens):
         swapped += evens[i]
      if i < len(odds):
         swapped += odds[i]
      i += 1
   print (swapped)

def main():
   swap_adjacent(sys.argv[1])

if __name__ == '__main__':
   main()