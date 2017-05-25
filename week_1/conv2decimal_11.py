import sys

def conv2decimal(n,base):
   total = 0
   power = 0
   for num in n[::-1]:
      total += int(num) * int(base) ** power
      power += 1
   return total

print (conv2decimal(sys.argv[1],sys.argv[2]))