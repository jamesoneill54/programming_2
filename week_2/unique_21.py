import sys
import string

def unique_token_count(text):
   text = text.strip().split()
   a = []
   for word in text:
      word = word.lower().strip(string.punctuation)
      if word not in a and word != '':
         a.append(word)
   return len(a)

def main():
   print (unique_token_count(sys.stdin.read()))

if __name__ == '__main__':
   main()