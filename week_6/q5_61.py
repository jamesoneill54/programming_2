import sys

def main():
   teams = {}
   longest_name = 0
   longest_score = 0
   for line in sys.stdin:
      try:
         name, points = line.strip().split(':')
         if len(name) > longest_name:
            longest_name = len(name)
         points = sum([int(p) for p in points.split()])
         if len(str(points)) > longest_score:
            longest_score = len(str(points))
         teams[points] = name
      except ValueError:
         continue
   for key in sorted(teams, reverse = True):
      print ('{:>{:d}s}: {:>{:d}d} points'.format(teams[key], longest_name, key, longest_score))

if __name__ == '__main__':
   main()