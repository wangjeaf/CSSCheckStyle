import os
homedir = os.getenv('USERPROFILE') or os.getenv('HOME')
print os.path.realpath(os.path.join(homedir, 'ckstyle.ini'))
