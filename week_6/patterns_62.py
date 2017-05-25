import sys
import re

dates_w_slashes = re.compile(r'\b\d{1,2}/{1}\d{1,2}/{1}\d{2}\b')
dates_w_hyphens = re.compile(r'\b\d{1,2}-{1}\d{1,2}-{1}\d{2}\b')
slashes_or_hyphens = re.compile(r'\b\d{1,2}[/-]{1}\d{1,2}[/-]{1}\d{2}\b')
dublin_phone = re.compile(r'\b(?:01)[-\s]{1}\d{7}\b')
emails = re.compile(r'\b[a-z]+(?:.{1}[a-z]+)*@{1}(?:[a-z]+.{1})+[a-z]+\b')
informal_dates = re.compile(r'\b\d{1,2}\s{1}(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec){1}\s{1}(?:\d{2}|\d{4}){1}\b')

def main():
   line = sys.stdin.read()
   print(dates_w_slashes.findall(line))
   print(dates_w_hyphens.findall(line))
   print(slashes_or_hyphens.findall(line))
   print(dublin_phone.findall(line))
   print(emails.findall(line))
   print(informal_dates.findall(line))

if __name__ == '__main__':
   main()