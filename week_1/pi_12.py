import sys
from math import pi

decimal_place = int(sys.argv[1])

print ('{:.{}f}'.format(pi, decimal_place))