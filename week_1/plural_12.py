import sys

vowels = ['a','e','i','o','u']

es_endings = {
   'ch' : 'es',
   'sh' : 'es',
   'x' : 'es',
   's' : 'es',
   'z' : 'es',
   'o' : 'es',
}

words = sys.stdin.readlines()

for noun in words:
   noun = noun.strip()
   if noun[-2:] in es_endings or noun[-1] in es_endings:
      for s in es_endings:
         if noun.endswith(s):
            print (noun + 'es')

   elif noun[-2] not in vowels and noun [-1] == 'y': 
      print (noun[:-1] + 'ies')

   elif noun.endswith('f'):
      print (noun[:-1] + 'ves')

   elif noun.endswith('fe'):
      print (noun[:-2] + 'ves')

   else: 
      print (noun + 's')