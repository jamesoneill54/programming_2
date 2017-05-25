import sys

n = int(sys.argv[1])

print ('Multiples of 3:', [n for n in range(1, n + 1) if not n % 3])
print ('Multiples of 3 squared:', [n ** 2 for n in range(1, n + 1) if not n % 3])
print ('Multiples of 4 doubled:', [n * 2 for n in range(1, n + 1) if not n % 4])
print ('Multiples of 3 or 4:', [n for n in range(1, n + 1) if not(n % 3 and n % 4)])
print ('Multiples of 3 and 4:', [n for n in range(1, n + 1) if not(n % 3 or n % 4)])
print ('Multiples of 3 replaced:', [n if n % 3 else 'X' for n in range(1, n + 1)])