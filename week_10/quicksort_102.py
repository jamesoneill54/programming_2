def partition(a, p, r):
   q = j = p 
   while j < r:
      if a[j] <= a[r]:
         a[q], a[j] = a[j], a[q]
         q += 1
      j += 1
   a[q], a[r] = a[r], a[q]
   return q

def quicksort(a, p, r):
   if r <= p:
      return
   q = partition(a, p, r)
   quicksort(a, p, q - 1)
   quicksort(a, q + 1, r)