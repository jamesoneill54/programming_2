import sys

months = {
   'January' : '1',
   'February' : '2',
   'March' : '3',
   'April' : '4',
   'May' : '5',
   'June' : '6',
   'July' : '7',
   'August' : '8',
   'September' : '9',
   'October' : '10',
   'November' : '11',
   'December' : '12'
}

def short_date(a):
   print ('{:s}/{:s}/{:s}'.format(a[0], months[a[1]], a[2][2:]))

def main():
   for line in sys.stdin:
      short_date(line.strip().split())

if __name__ == '__main__':
   main()