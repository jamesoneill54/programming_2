class File(object):

   FILE_PERMISSIONS = 'rwx'

   def __init__(self, name, owner, size=0, permissions=None):
      self.name = name
      self.owner = owner
      self.size = size
      if permissions:
         self.permissions = ''.join(sorted(permissions))
      else:
         self.permissions = 'null'

   def __str__(self):
      return 'File: {:s}\nOwner: {:s}\nPermissions: {:s}\nSize: {:d} bytes'.format(self.name, self.owner,
                                                                                   self.permissions, self.size)

   def has_access(self, user, permission):
      if self.owner == user:
         return True
      elif permission in self.permissions:
         return True
      return False