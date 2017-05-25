import sys
import calendar

# sys.arg comes in as dd, mm, yyyy.
# calendar.weekday(1970-, 1-12, 1-31)
poem = {
   0 : 'is fair of face',
   1 : 'is full of grace',
   2 : 'is full of woe',
   3 : 'has far to go',
   4 : 'is loving and giving',
   5 : 'works hard for a living',
   6 : 'is fair and wise and good in every way'
}

weekdays = {
   0 : 'Monday',
   1 : 'Tuesday',
   2 : 'Wednesday',
   3 : 'Thursday',
   4 : 'Friday',
   5 : 'Saturday',
   6 : 'Sunday'
}

def birthday(dob):
   [year, month, day] = dob
   day = calendar.weekday(int(year), int(month), int(day))
   return "You were born on a {} and {}'s child {}.".format(weekdays[day], weekdays[day], poem[day])

def main():
   dob = sys.argv[:0:-1]
   print (birthday(dob))

if __name__ == '__main__':
   main()