import sys
from collections import namedtuple

Student = namedtuple('Student', ['firstname', 'surname', 'id'])

def show_student(student):
   print ('{:>10s}: {:<s}'.format('First name', student.firstname))
   print ('{:>10s}: {:<s}'.format('Surname', student.surname))
   print ('{:>10s}: {:<d}'.format('ID', student.id))