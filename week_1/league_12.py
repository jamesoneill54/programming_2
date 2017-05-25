import sys

def league_table(lines):
   longest_club = 0
   for line in lines:
      line = line.split()
      club_name = ' '.join(line[1:-8])
      if len(club_name) > longest_club:
         longest_club = len(club_name)
   print ('{:3s} {:<{}s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}'.format('POS', 'CLUB', longest_club, 'P', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'PTS'))

   for line in lines:
      line = line.strip().split()
      print ('{:>3s} {:<{}s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}'.format(line[0], ' '.join(line[1:-8]), longest_club, line[-8], line[-7], line[-6], line[-5], line[-4], line[-3], line[-2], line[-1]))


def main():
   lines = sys.stdin.readlines()

   league_table(lines)

if __name__ == '__main__':
   main()