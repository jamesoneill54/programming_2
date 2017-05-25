import sys
from stack_92 import Stack 

def matcher(line):

   parentheses = {')': '(',
                  '}': '{',
                  ']': '['}
   s = Stack()
   for c in line:
      if c in parentheses.values():
         s.push(c)
      elif not s.is_empty() and parentheses[c] == s.top():
         s.pop()
      else:
         return False
   return s.is_empty()