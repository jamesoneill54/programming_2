import sys

def print_evil(s):
   word = s.strip().lower()
   to_check = 'evil'
   i = 0
   j = 0
   while j < len(word):
      if word[j] in to_check[:i]:
         break
      if i < len(to_check) and word[j] == to_check[i]:
         i += 1
      j += 1
   if j == len(word) and i == len(to_check):
      print (s.strip())

def main():
   for line in sys.stdin:
      print_evil(line)

if __name__ == '__main__':
   main()