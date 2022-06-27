import os
if os.name == 'nt':
    home = os.getenv('USERPROFILE')
else:
    home = os.getenv('HOME')
desktop_dir = os.path.join(home, 'Desktop')
print(desktop_dir)
