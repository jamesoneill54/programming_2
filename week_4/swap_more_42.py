import sys

def swap_unique_keys_values(d):
   keys = []
   values = []
   uniqueness = []
   swapped_unique_d = {}
   for key in d:
      keys.append(key)
      values.append(d[key])
   
   for item in keys:
      uniqueness.append(True)

   i = 0
   while i < len(keys):
      p = i + 1
      while p < len(values):
         if values[i] == values[p]:
            uniqueness[i] = False
            uniqueness[p] = False
         p += 1
      i += 1

   j = 0
   while j < len(uniqueness):
      if uniqueness[j]:
         swapped_unique_d[values[j]] = keys[j]
      j += 1
   return swapped_unique_d

def main():
   a_dict = {'a' : 3, 'b' : 2, 'f' : 3, 'g' : 6, 'r' : 4, 'p' : 5, 'e' : 2}
   print (swap_unique_keys_values(a_dict))

if __name__ == '__main__':
   main()