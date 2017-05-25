def power(m, n):
   if n == 1:
      return m
   if n < 1:
      return 1
   return m * power(m, n - 1)