def swap_first_last(a, first, last):
   if first >= last:
      return
   a[first], a[last] = a[last], a[first]
   first += 1
   last -= 1
   swap_first_last(a, first, last)

def reverse_list(a):
   swap_first_last(a, 0, len(a) - 1)
   return a