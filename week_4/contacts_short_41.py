import sys

with open(sys.argv[1], 'r') as f:
   contacts = {}
   for line in f:
      [name, phone] = line.strip().split()
      contacts[name] = phone

for line in sys.stdin:
   if line.strip() in contacts: 
      print('Name:', line.strip())
      print('Phone:', contacts[line.strip()])
   else:
      print('Name:', line.strip())
      print('No such contact')