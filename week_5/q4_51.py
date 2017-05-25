import sys

def measures_of_centre(a):
   frequency = {}
   total = 0
   for n in a:
      if n in frequency:
         frequency[n] += 1
      else:
         frequency[n] = 1
      total += n
   mean = float(total / len(a))
   mode = 0
   for key in frequency:
      if frequency[key] > mode:
         mode = float(key)
   if len(a) % 2 == 0:
      middle_1 = float(sorted(a)[int(len(a) / 2)])
      middle_2 = float(sorted(a)[int((len(a) / 2) - 1)])
      median = (middle_1 + middle_2) / 2
   else:
      median = float(sorted(a)[int(len(a) / 2)])
   print ('Mean: {:.1f}'.format(mean))
   print ('Mode: {:.1f}'.format(mode))
   print ('Median: {:.1f}'.format(median))

def main():
   a = []
   for line in sys.stdin:
      a.append(int(line.strip()))
   measures_of_centre(a)

if __name__ == '__main__':
   main()