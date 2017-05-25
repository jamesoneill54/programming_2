import sys

class Contact(object):
   
   def __init__(self, name, phone, email):
      self.name = name
      self.phone = phone
      self.email = email

   def __str__(self):
      return '{:s} {:s} {:s}'.format(self.name, self.phone, self.email)

class ContactList(object):

   def __init__(self, d=None):
      if not d:
         self.d = {}
      else:
         self.d = d 

   def add_contact(self, contact):
      self.d[contact.name] = contact

   def del_contact(self, name):
      if name in self.d:
         del self.d[name]

   def get_contact(self, name):
      if name in self.d:
         return self.d[name]
      return '{:s} : No such contact'.format(name)

   def __str__(self):
      title = 'Contact list'
      dividers = '-' * len(title)
      a = [title, dividers]
      for item in sorted(self.d):
         a.append(self.d[item].__str__())
      return '\n'.join(a)