import sys

points = {
   -7 : 9,
   -6 : 8,
   -5 : 7,
   -4 : 6,
   -3 : 5,
   -2 : 4,
   -1 : 3,
   0 : 2,
   1 : 1
}

def stableford_scores(pars, indexes, handicap, strokes):
   #calculate free strokes
   free_18, extra_free = divmod(handicap, 18)
   free_strokes = [] #poisition refers to index number
   i = 0
   while i < 18:
      if extra_free > i:
         free_strokes.append(free_18 + 1)
      else: 
         free_strokes.append(free_18)
      i += 1


   #calculate score_to_par
   score_to_par = [] #position refers to hole number
   hole = 0
   while hole < len(strokes):
      if strokes[hole] != 'X':
         index_pos = indexes[hole] - 1
         score_to_par.append((strokes[hole] - free_strokes[index_pos]) - pars[hole])
      else:
         score_to_par.append('X')
      hole += 1


   #calculate points
   total = 0
   for h in score_to_par:
      if type(h) == int:
         if h in points:
            total += points[h]
   return total



def main():
   pars = False
   indexes = False
   player_scores = {}      # {scores : player_names}
   disqualified = []
   longest_name = 0
   longest_score = 0
   

   for line in sys.stdin:
      if not pars:
         pars = [int(p) for p in line.strip().split()]
         continue
      if not indexes:
         indexes = [int(i) for i in line.strip().split()]
         continue
      player = line.strip().split()
      name = ' '.join(player[:-19])
      if len(name) > longest_name:
         longest_name = len(name)
      handicap = int(player[-19])
      

      #getting strokes
      strokes = []
      for s in player[-18:]:
         if s.isdigit():
            strokes.append(int(s))
            continue
         if s == 'X':
            strokes.append(s)
            continue
         disqualified.append(name)
         break
      if name in disqualified:
         continue


      #getting scores
      score = stableford_scores(pars, indexes, handicap, strokes)
      if len(str(score)) > longest_score:
         longest_score = len(str(score))
      player_scores[score] = name
   
   out = []
   for score in sorted(player_scores, reverse = True):
      out.append('{:>{:d}s} : {:>{:d}d}'.format(player_scores[score], longest_name, score, longest_score))
   for name in disqualified:
      out.append('{:>{:d}s} : Disqualified'.format(name, longest_name))
   print('\n'.join(out))


if __name__ == '__main__':
   main()