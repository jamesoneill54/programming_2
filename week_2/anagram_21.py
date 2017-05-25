import sys

def anagram(line):
   line = line.split()
   if len(line[0]) == len(line[1]):
      word_1 = line[0]
      word_2 = line[1]
      for char in word_1:
         if char in word_2:
            word_2 = word_2.replace(char, '')
      if word_2 == '':
         return True
   return False   

for line in sys.stdin:
   print (anagram(line))