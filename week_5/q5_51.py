import sys

def seconds(s):
   [minutes, seconds] = s.split(":")
   total = int(minutes) * 60 + int(seconds)
   return total

def sorter(t):
   return seconds(t[-1])

def main():
   d = {}
   for line in sys.stdin:
      try:
         split_up = line.strip().split()
         d[split_up[0]] = min(split_up[1:], key = seconds)
      except ValueError:
         continue
   winner = min(d.items(), key = sorter)
   print("{} : {}".format(winner[0], winner[1]))

if __name__ == "__main__":
   main()