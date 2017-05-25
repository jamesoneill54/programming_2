import sys

def swap_keys_values(d):
   swapped_d = {}
   for key in d:
      swapped_d[d[key]] = key
   return swapped_d

def main():
   a_dict = {1 : 'a', 2 : 'b', 3 : 'c'}
   print (swap_keys_values(a_dict))

if __name__ == '__main__':
   main()