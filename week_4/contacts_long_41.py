import sys

with open(sys.argv[1], 'r') as f:
   contacts = {}
   for line in f:
      [name, phone, email] = line.strip().split()
      contacts[name] = [phone, email]

for line in sys.stdin:
   if line.strip() in contacts: 
      print('Name:', line.strip())
      print('Phone:', contacts[line.strip()][0])
      print('Email:', contacts[line.strip()][1])
   else:
      print('Name:', line.strip())
      print('No such contact')