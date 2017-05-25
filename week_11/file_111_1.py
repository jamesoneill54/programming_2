class File(object):

   FILE_PERMISSIONS = 'rwx'

   def __init__(self, name, owner, size=0, permissions=None):
      self.name = name
      self.owner = owner
      self.size = size
      if self.permissions:
         self.permissions = ''.join(sorted(self.permissions))
      else:
         self.permissions = 'null'

   def __str__(self):
      return 'File: {:s}\n'