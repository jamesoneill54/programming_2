import sys

# S.lower() to convert all chars to lower case.
# S.isalnum() to check if the char is alphanumeric.

def palindrome(line):
   line = line.strip().lower()
   for char in line:
      if not char.isalnum():
         line = line.replace(char, '')
   if line == line[::-1]:
      return True
   return False

def main():
   for line in sys.stdin:
      print (palindrome(line))

if __name__ == '__main__':
   main()