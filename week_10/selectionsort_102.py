def selectionsort(a):
   i = 0
   while i < len(a):
      j = 0
      while j < len(a):
         if a[j] > a[i]:
            a[i], a[j] = a[j], a[i]
         j += 1
      i += 1