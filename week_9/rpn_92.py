import sys
from stack_92 import Stack

def add(e1, e2):
   return float(e1 + e2)

def minus(e2, e1):
   return float(e1 - e2)

def multiply(e1, e2):
   return float(e1 * e2)

def divide(e2, e1):
   return float(e1 / e2)

def negate(e):
   return float(e * -1)

def root(e):
   return float(e ** (1 / 2))

binops = {
   '+': add,
   '-': minus,
   '*': multiply,
   '/': divide
}

uniops = {
   'n': negate,
   'r': root
}

def calculator(line):
   rpn = Stack()
   line = line.strip().split()
   for e in line:
      if e in binops:
         rpn.push(binops[e](float(rpn.pop()), float(rpn.pop())))
         continue
      if e in uniops:
         rpn.push(uniops[e](float(rpn.pop())))
         continue
      rpn.push(float(e))
   if len(rpn) != 1:
      return IndexError
   return rpn.top()