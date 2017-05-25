import sys
import re

def email_addresses(line):
   email = re.compile(r'\b\w+(?:\.\w+)*@\w+\.\w+(?:\.\w+)*\b')
   addresses = email.findall(line)
   for e in addresses:
      name, domain = e.strip().split('@')
      name = name.split('.')
      out = [s.capitalize() for s in name]
      print (' '.join(out))

def main():
   for line in sys.stdin:
      email_addresses(line)

if __name__ == '__main__':
   main()